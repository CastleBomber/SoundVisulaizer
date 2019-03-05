#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time

##
# Spits out cBombs (5 seconds)
#
class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("../../../fonts/5x7.bdf")

        red = graphics.Color(255, 0, 0)
        graphics.DrawText(canvas, font, 1, 30, red, "cBombs")

        time.sleep(2)


##
# Trying to then make it spit colors
#
class PulsingColors(SampleBase):
    def __init__(self, *args, **kwargs):
        super(PulsingColors, self).__init__(*args, **kwargs)

    def run(self):
        ##+++++++
        ##        canvas = self.matrix
        ##        font = graphics.Font()
        ##        font.LoadFont("../../../fonts/5x7.bdf")
        ##
        ##        red = graphics.Color(255, 0, 0)
        ##        graphics.DrawText(canvas, font, 1, 30, red, "cBombs")
        ##
        ##        time.sleep(2)
        ##+++++++++++

        self.offscreen_canvas = self.matrix.CreateFrameCanvas()
        continuum = 0

        while True:
            #self.usleep(5 * 1000) # mat sleeps
            self.usleep(.4 / 1000)
            continuum += 1
            continuum %= 3 * 255

            red = 0
            green = 0
            blue = 0

            if continuum <= 255:
                c = continuum
                blue = 255 - c
                red = c
            elif continuum > 255 and continuum <= 511:
                c = continuum - 256
                red = 255 - c
                green = c
            else:
                c = continuum - 512
                green = 255 - c
                blue = c

            self.offscreen_canvas.Fill(red, green, blue)
            self.offscreen_canvas = self.matrix.SwapOnVSync(self.offscreen_canvas)



# Main function
if __name__ == "__main__":
    pulsing_colors = PulsingColors()
    if (not pulsing_colors.process()):
        pulsing_colors.print_help()

