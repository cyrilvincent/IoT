# MicroPython SSD1306 OLED driver, I2C and SPI interfaces created by Adafruit

from micropython import const
import framebuf


# register definitions
SET_CONTRAST        = const(0x81)
SET_ENTIRE_ON       = const(0xa4)
SET_NORM_INV        = const(0xa6)
SET_DISP            = const(0xae)
SET_MEM_ADDR        = const(0x20)
SET_COL_ADDR        = const(0x21)
SET_PAGE_ADDR       = const(0x22)
SET_DISP_START_LINE = const(0x40)
SET_SEG_REMAP       = const(0xa0)
SET_MUX_RATIO       = const(0xa8)
SET_COM_OUT_DIR     = const(0xc0)
SET_DISP_OFFSET     = const(0xd3)
SET_COM_PIN_CFG     = const(0xda)
SET_DISP_CLK_DIV    = const(0xd5)
SET_PRECHARGE       = const(0xd9)
SET_VCOM_DESEL      = const(0xdb)
SET_CHARGE_PUMP     = const(0x8d)


class SSD1306:
    def __init__(self, width, height, external_vcc, color=framebuf.MONO_VLSB):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.pages = self.height // 8
        self.buffer = bytearray(self.pages * self.width)
        fb = framebuf.FrameBuffer(self.buffer, self.width, self.height, color)
        self.framebuf = fb
        # Provide methods for accessing FrameBuffer graphics primitives. This is a
        # workround because inheritance from a native class is currently unsupported.
        # http://docs.micropython.org/en/latest/pyboard/library/framebuf.html
        self.fill = fb.fill
        self.pixel = fb.pixel
        self.hline = fb.hline
        self.vline = fb.vline
        self.line = fb.line
        self.rect = fb.rect
        self.fill_rect = fb.fill_rect
        self.text = fb.text
        self.scroll = fb.scroll
        self.blit = fb.blit
        self.init_display()

    def init_display(self):
        for cmd in (
            SET_DISP | 0x00, # off
            # address setting
            SET_MEM_ADDR, 0x00, # horizontal
            # resolution and layout
            SET_DISP_START_LINE | 0x00,
            SET_SEG_REMAP | 0x01, # column addr 127 mapped to SEG0
            SET_MUX_RATIO, self.height - 1,
            SET_COM_OUT_DIR | 0x08, # scan from COM[N] to COM0
            SET_DISP_OFFSET, 0x00,
            SET_COM_PIN_CFG, 0x02 if self.height == 32 else 0x12,
            # timing and driving scheme
            SET_DISP_CLK_DIV, 0x80,
            SET_PRECHARGE, 0x22 if self.external_vcc else 0xf1,
            SET_VCOM_DESEL, 0x30, # 0.83*Vcc
            # display
            SET_CONTRAST, 0xff, # maximum
            SET_ENTIRE_ON, # output follows RAM contents
            SET_NORM_INV, # not inverted
            # charge pump
            SET_CHARGE_PUMP, 0x10 if self.external_vcc else 0x14,
            SET_DISP | 0x01): # on
            self.write_cmd(cmd)
        self.fill(0)
        self.show()

    def poweroff(self):
        self.write_cmd(SET_DISP | 0x00)

    def poweron(self):
        self.write_cmd(SET_DISP | 0x01)

    def contrast(self, contrast):
        self.write_cmd(SET_CONTRAST)
        self.write_cmd(contrast)

    def invert(self, invert):
        self.write_cmd(SET_NORM_INV | (invert & 1))

    def show(self):
        x0 = 0
        x1 = self.width - 1
        if self.width == 64:
            # displays with width of 64 pixels are shifted by 32
            x0 += 32
            x1 += 32
        self.write_cmd(SET_COL_ADDR)
        self.write_cmd(x0)
        self.write_cmd(x1)
        self.write_cmd(SET_PAGE_ADDR)
        self.write_cmd(0)
        self.write_cmd(self.pages - 1)
        self.write_data(self.buffer)


class SSD1306_I2C(SSD1306):
    def __init__(self, width, height, i2c, addr=0x3c, external_vcc=False, color=framebuf.MONO_VLSB):
        self.i2c = i2c
        self.addr = addr
        self.temp = bytearray(2)
        super().__init__(width, height, external_vcc, color)

    def write_cmd(self, cmd):
        self.temp[0] = 0x80 # Co=1, D/C#=0
        self.temp[1] = cmd
        self.i2c.writeto(self.addr, self.temp)

    def write_data(self, buf):
        self.i2c.writeto(self.addr, b'\x40' + buf)


class SSD1306_SPI(SSD1306):
    def __init__(self, width, height, spi, dc, res, cs, external_vcc=False, color=framebuf.MONO_VLSB):
        self.rate = 10 * 1024 * 1024
        dc.init(dc.OUT, value=0)
        res.init(res.OUT, value=0)
        cs.init(cs.OUT, value=1)
        self.spi = spi
        self.dc = dc
        self.res = res
        self.cs = cs
        import time
        self.res(1)
        time.sleep_ms(1)
        self.res(0)
        time.sleep_ms(10)
        self.res(1)
        super().__init__(width, height, external_vcc, color)

    def write_cmd(self, cmd):
        self.spi.init(baudrate=self.rate, polarity=0, phase=0)
        self.cs(1)
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)

    def write_data(self, buf):
        self.spi.init(baudrate=self.rate, polarity=0, phase=0)
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(buf)
        self.cs(1)
        
        
class GFX:

    def __init__(self, width, height, pixel, hline=None, vline=None):
        # Create an instance of the GFX drawing class.  You must pass in the
        # following parameters:
        #  - width = The width of the drawing area in pixels.
        #  - height = The height of the drawing area in pixels.
        #  - pixel = A function to call when a pixel is drawn on the display.
        #            This function should take at least an x and y position
        #            and then any number of optional color or other parameters.
        #  You can also provide the following optional keyword argument to
        #  improve the performance of drawing:
        #  - hline = A function to quickly draw a horizontal line on the display.
        #            This should take at least an x, y, and width parameter and
        #            any number of optional color or other parameters.
        #  - vline = A function to quickly draw a vertical line on the display.
        #            This should take at least an x, y, and height paraemter and
        #            any number of optional color or other parameters.
        self.width = width
        self.height = height
        self._pixel = pixel
        # Default to slow horizontal & vertical line implementations if no
        # faster versions are provided.
        if hline is None:
            self.hline = self._slow_hline
        else:
            self.hline = hline
        if vline is None:
            self.vline = self._slow_vline
        else:
            self.vline = vline

    def _slow_hline(self, x0, y0, width, *args, **kwargs):
        # Slow implementation of a horizontal line using pixel drawing.
        # This is used as the default horizontal line if no faster override
        # is provided.
        if y0 < 0 or y0 > self.height or x0 < -width or x0 > self.width:
            return
        for i in range(width):
            self._pixel(x0+i, y0, *args, **kwargs)

    def _slow_vline(self, x0, y0, height, *args, **kwargs):
        # Slow implementation of a vertical line using pixel drawing.
        # This is used as the default vertical line if no faster override
        # is provided.
        if y0 < -height or y0 > self.height or x0 < 0 or x0 > self.width:
            return
        for i in range(height):
            self._pixel(x0, y0+i, *args, **kwargs)

    def rect(self, x0, y0, width, height, *args, **kwargs):
        # Rectangle drawing function.  Will draw a single pixel wide rectangle
        # starting in the upper left x0, y0 position and width, height pixels in
        # size.
        if y0 < -height or y0 > self.height or x0 < -width or x0 > self.width:
            return
        self.hline(x0, y0, width, *args, **kwargs)
        self.hline(x0, y0+height-1, width, *args, **kwargs)
        self.vline(x0, y0, height, *args, **kwargs)
        self.vline(x0+width-1, y0, height, *args, **kwargs)

    def fill_rect(self, x0, y0, width, height, *args, **kwargs):
        # Filled rectangle drawing function.  Will draw a single pixel wide
        # rectangle starting in the upper left x0, y0 position and width, height
        # pixels in size.
        if y0 < -height or y0 > self.height or x0 < -width or x0 > self.width:
            return
        for i in range(x0, x0+width):
            self.vline(i, y0, height, *args, **kwargs)

    def line(self, x0, y0, x1, y1, *args, **kwargs):
        # Line drawing function.  Will draw a single pixel wide line starting at
        # x0, y0 and ending at x1, y1.
        steep = abs(y1 - y0) > abs(x1 - x0)
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        dx = x1 - x0
        dy = abs(y1 - y0)
        err = dx // 2
        ystep = 0
        if y0 < y1:
            ystep = 1
        else:
            ystep = -1
        while x0 <= x1:
            if steep:
                self._pixel(y0, x0, *args, **kwargs)
            else:
                self._pixel(x0, y0, *args, **kwargs)
            err -= dy
            if err < 0:
                y0 += ystep
                err += dx
            x0 += 1

    def circle(self, x0, y0, radius, *args, **kwargs):
        # Circle drawing function.  Will draw a single pixel wide circle with
        # center at x0, y0 and the specified radius.
        f = 1 - radius
        ddF_x = 1
        ddF_y = -2 * radius
        x = 0
        y = radius
        self._pixel(x0, y0 + radius, *args, **kwargs)
        self._pixel(x0, y0 - radius, *args, **kwargs)
        self._pixel(x0 + radius, y0, *args, **kwargs)
        self._pixel(x0 - radius, y0, *args, **kwargs)
        while x < y:
            if f >= 0:
                y -= 1
                ddF_y += 2
                f += ddF_y
            x += 1
            ddF_x += 2
            f += ddF_x
            self._pixel(x0 + x, y0 + y, *args, **kwargs)
            self._pixel(x0 - x, y0 + y, *args, **kwargs)
            self._pixel(x0 + x, y0 - y, *args, **kwargs)
            self._pixel(x0 - x, y0 - y, *args, **kwargs)
            self._pixel(x0 + y, y0 + x, *args, **kwargs)
            self._pixel(x0 - y, y0 + x, *args, **kwargs)
            self._pixel(x0 + y, y0 - x, *args, **kwargs)
            self._pixel(x0 - y, y0 - x, *args, **kwargs)

    def fill_circle(self, x0, y0, radius, *args, **kwargs):
        # Filled circle drawing function.  Will draw a filled circule with
        # center at x0, y0 and the specified radius.
        self.vline(x0, y0 - radius, 2*radius + 1, *args, **kwargs)
        f = 1 - radius
        ddF_x = 1
        ddF_y = -2 * radius
        x = 0
        y = radius
        while x < y:
            if f >= 0:
                y -= 1
                ddF_y += 2
                f += ddF_y
            x += 1
            ddF_x += 2
            f += ddF_x
            self.vline(x0 + x, y0 - y, 2*y + 1, *args, **kwargs)
            self.vline(x0 + y, y0 - x, 2*x + 1, *args, **kwargs)
            self.vline(x0 - x, y0 - y, 2*y + 1, *args, **kwargs)
            self.vline(x0 - y, y0 - x, 2*x + 1, *args, **kwargs)

    def triangle(self, x0, y0, x1, y1, x2, y2, *args, **kwargs):
        # Triangle drawing function.  Will draw a single pixel wide triangle
        # around the points (x0, y0), (x1, y1), and (x2, y2).
        self.line(x0, y0, x1, y1, *args, **kwargs)
        self.line(x1, y1, x2, y2, *args, **kwargs)
        self.line(x2, y2, x0, y0, *args, **kwargs)

    def fill_triangle(self, x0, y0, x1, y1, x2, y2, *args, **kwargs):
        # Filled triangle drawing function.  Will draw a filled triangle around
        # the points (x0, y0), (x1, y1), and (x2, y2).
        if y0 > y1:
            y0, y1 = y1, y0
            x0, x1 = x1, x0
        if y1 > y2:
            y2, y1 = y1, y2
            x2, x1 = x1, x2
        if y0 > y1:
            y0, y1 = y1, y0
            x0, x1 = x1, x0
        a = 0
        b = 0
        y = 0
        last = 0
        if y0 == y2:
            a = x0
            b = x0
            if x1 < a:
                a = x1
            elif x1 > b:
                b = x1
            if x2 < a:
                a = x2
            elif x2 > b:
                b = x2
            self.hline(a, y0, b-a+1, *args, **kwargs)
            return
        dx01 = x1 - x0
        dy01 = y1 - y0
        dx02 = x2 - x0
        dy02 = y2 - y0
        dx12 = x2 - x1
        dy12 = y2 - y1
        if dy01 == 0:
            dy01 = 1
        if dy02 == 0:
            dy02 = 1
        if dy12 == 0:
            dy12 = 1
        sa = 0
        sb = 0
        if y1 == y2:
            last = y1
        else:
            last = y1-1
        for y in range(y0, last+1):
            a = x0 + sa // dy01
            b = x0 + sb // dy02
            sa += dx01
            sb += dx02
            if a > b:
                a, b = b, a
            self.hline(a, y, b-a+1, *args, **kwargs)
        sa = dx12 * (y - y1)
        sb = dx02 * (y - y0)
        while y <= y2:
            a = x1 + sa // dy12
            b = x0 + sb // dy02
            sa += dx12
            sb += dx02
            if a > b:
                a, b = b, a
            self.hline(a, y, b-a+1, *args, **kwargs)
            y += 1    
        
