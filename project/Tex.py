from manim import *


class EXPRESSION(Scene):
    def ORIGIN():
        Equa = Tex(r"$L = \int_0^1 \sqrt{1 + (\frac{dy}{dx})^2} dx$", font_size=48)
        msg = Text("Ta thấy dạng: ", font_size=24).next_to(Equa, DOWN)
        msgTex = Tex(r"$\sqrt{1+x^2}$", font_size=48, color=GREEN).next_to(msg, RIGHT)
        return Equa, msg, msgTex

    def SECOND():
        vertices = [
            np.array([-2, -1.5, 0]),
            np.array([2, -1.5, 0]),
            np.array([-2, 1.5, 0]),
        ]
        rightAngledTriangle = Polygon(
            *vertices,
            fill_color=BLUE,
            fill_opacity=0.6,
            stroke_color=BLUE,
            stroke_width=2
        )
        labelOffset = [
            np.array([-2.5, 0, 0]),
            np.array([0, -2, 0]),
            np.array([0, 1.2, 0]),
        ]
        labels = ["1", "x", r"$\sqrt{1+x^2}$"]
        triangleLabel = [Tex(labels[i]).move_to(labelOffset[i]) for i in range(3)]
        PhiAngle = Angle.from_three_points(
            vertices[0],
            vertices[1],
            vertices[2],
            radius=0.5,
            color=GREEN,
            other_angle=True,
        )

        return rightAngledTriangle, triangleLabel, PhiAngle

    def THIRD():
        pass
