from manim import *

from Tex import EXPRESSION


class MASTER(Scene):
    def Axis_INIT(self):
        Axis = (
            Axes(
                x_range=[-1, 2, 0.5],
                y_range=[-1, 2, 0.5],
                x_length=8,
                y_length=6,
                tips=True,
            )
            .add_coordinates()
            .to_edge(DOWN)
        )
        axisLabel = Axis.get_axis_labels(x_label="x(mi)", y_label="y(mi)")
        return Axis, axisLabel

    def Func_INIT(self):
        Axis, _ = self.Axis_INIT()

        Func = Axis.plot(lambda x: 0.5 * x**2, color=YELLOW, x_range=[0, 1.5, 0.3])
        funcLabel = (
            MathTex("y = 1/2{x}^{2}")
            .scale(0.8)
            .next_to(Func, UR, buff=0.3)
            .set_color(YELLOW)
        )
        return Func, funcLabel

    def Func_ANIMATE(self):
        Axis, _ = self.Axis_INIT()

        FuncHighlight = Axis.plot(
            lambda x: 0.5 * x**2, color=PURPLE, x_range=[0, 1, 0.1]
        )
        Equa = Tex(r"$L = \int_0^1 \sqrt{1 + (\frac{dy}{dx})^2} dx$", font_size=32)
        Equa.shift(UP, RIGHT)
        return FuncHighlight, Equa

    def POINT_INIT(self):
        Axis, _ = self.Axis_INIT()
        pointA = Dot(color=RED).move_to(Axis.c2p(0, 0))
        pointB = Dot(color=BLUE).move_to(Axis.c2p(1, 0.5))
        pointALabel = MathTex("A(0; 0)").scale(0.5).next_to(pointA, DR).set_color(RED)
        pointBLabel = MathTex("B(1; 1/2)").scale(0.5).next_to(pointB).set_color(BLUE)
        return pointA, pointB, pointALabel, pointBLabel

    def ERASE(self, obj):
        self.play(Unwrite(obj))

    def construct(self):
        Axis, axisLabel = self.Axis_INIT()
        Func, funcLabel = self.Func_INIT()
        pointA, pointB, pointALabel, pointBLabel = self.POINT_INIT()
        FuncHighlight, Equa = self.Func_ANIMATE()

        # Init & animate objs on the screen
        self.play(FadeIn(VGroup(Axis, axisLabel)), run_time=3)
        self.play(DrawBorderThenFill(Func), run_time=5)
        self.wait(0.5)
        self.play(Write(funcLabel), run_time=2)
        self.play(Create(VGroup(pointA, pointB, pointALabel, pointBLabel)), run_time=2)
        self.wait(1)
        self.play(Create(FuncHighlight), run_time=3)
        self.play(Write(Equa))
        self.wait(2)

        # Erase everything in sequence
        self.ERASE(
            VGroup(
                Func,
                funcLabel,
                pointA,
                pointB,
                pointALabel,
                pointBLabel,
                FuncHighlight,
                Equa,
            ),
        )
        self.ERASE(VGroup(Axis, axisLabel))

        # Proofing
        Equa, msg, msgTex = EXPRESSION.ORIGIN()
        line2 = VGroup(msg, msgTex).center()
        originPara = VGroup(Equa, line2)
        self.play(Write(Equa))
        self.wait(1)
        self.play(Write(line2), Equa.animate.shift(UP), run_time=2)

        triangle, triangleLabel = EXPRESSION.SECOND()
        self.play(
            DrawBorderThenFill(triangle),
            originPara.animate.to_corner(RIGHT),
            run_time=3,
        )
        self.play(*[Write(label) for label in triangleLabel])
        self.wait(1)

        self.ERASE(originPara)
        triangleGroup = VGroup(triangle, triangleLabel)
        # [self.ERASE(element) for element in triangleLabel]
        self.play(triangleGroup.animate.to_edge(UL))
        

        self.wait()
