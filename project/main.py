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

    def Func_ANIMATE(self, color=PURPLE):
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
        self.play(FadeOut(*self.mobjects))

        # Proofing
        # Scene 1
        Equa_proof, msg, msgTex = EXPRESSION.ORIGIN()
        line2 = VGroup(msg, msgTex).center()
        originPara = VGroup(Equa_proof, line2)
        self.play(Write(Equa_proof))
        self.wait(1)
        self.play(Write(line2), Equa_proof.animate.shift(UP), run_time=2)

        # Scene 2
        triangle, triangleLabel, PhiAngle = EXPRESSION.SECOND()
        self.play(
            DrawBorderThenFill(triangle),
            originPara.animate.to_corner(RIGHT),
            run_time=3,
        )
        self.play(*[Write(label) for label in triangleLabel])
        self.play(Create(PhiAngle))
        self.wait(1)
        self.ERASE(originPara)
        triangleGroup = VGroup(triangle, triangleLabel, PhiAngle)
        # [self.ERASE(element) for element in triangleLabel]
        self.play(triangleGroup.animate.to_edge(UL))

        # Scene 3
        title = Text("Ta đặt:", font_size=24).to_edge(UP)
        self.play(Write(title))

        line31 = (
            MathTex(r"x = \tan \theta", font_size=36)
            .next_to(title, DOWN)
            .shift(LEFT * 1.2)
        )
        line32 = MathTex(r"\quad \text{hay} \quad", font_size=36).next_to(title, DOWN)
        line33 = (
            MathTex(r"\theta = \arctan x", font_size=36)
            .next_to(title, DOWN)
            .shift(RIGHT * 1.5)
        )
        transform_label = VGroup(line31, line32, line33)
        self.play(Write(transform_label))
        line41 = MathTex(r"dx = sec^2 \theta d\theta", font_size=36).next_to(
            line31, DOWN, buff=0.4
        )
        line42 = MathTex(r"d\theta = \frac{dx}{1+x^2}", font_size=36).next_to(
            line33, DOWN
        )
        self.play(TransformFromCopy(line31, line41))
        self.play(TransformFromCopy(line33, line42))

        line51 = Text("Với :", font_size=24)
        line52 = MathTex(
            r"\frac{-\pi}{2} < \theta < \frac{\pi}{2}", font_size=36
        ).next_to(line51, RIGHT, buff=0.3)
        line5 = VGroup(line51, line52).next_to(line41, DOWN, buff=1)
        self.wait(2)
        self.play(FadeOut(*self.mobjects))

        integral_given_text = Text("Tích phân bất định đã biết:", font_size=24).to_edge(
            UP
        )
        line6 = MathTex(
            r"\int \sqrt{1+x^2} \, dx",
            r"=",
            r"\frac{1}{2} \left( x \sqrt{1+x^2} + \ln|x + \sqrt{1+x^2}| \right) + C",
            font_size=36,
        ).next_to(integral_given_text, DOWN)

        self.play(
            Write(integral_given_text),
        )
        self.wait(1)
        self.play(TransformFromCopy(integral_given_text, line6))

        line7 = MathTex(r"sec \theta = \sqrt{1+x^2}", font_size=36).next_to(line6, DOWN)
        L_def = MathTex(
            r"L", r"=", r"\int_{0}^{1} \sqrt{1+x^2} \, dx", font_size=36
        ).next_to(line7, DOWN, buff=1.0)

        self.play(Write(line7))
        self.play(TransformFromCopy(line6, L_def))
        self.wait(1)
        self.play(L_def.animate.shift(LEFT * 3))
        line81 = MathTex(
            r"=",
            r"\left[ \frac{1}{2} \left( x \sqrt{1+x^2} + \ln|x + \sqrt{1+x^2}| \right) \right]_{0}^{1}",
            font_size=36,
        ).next_to(L_def, RIGHT)
        self.play(Write(line81))
        self.wait(1)
        self.play(FadeOut(*self.mobjects))

        line9 = MathTex(
            r"\L = \left[ \frac{1}{2} \left( x \sqrt{1+x^2} + \ln|x + \sqrt{1+x^2}| \right) \right]_{0}^{1}"
        ).to_edge(UP)
        L_sub_1_target = (
            MathTex(
                r"L",
                r"=",
                r"\frac{1}{2} \left( 1 \sqrt{1+1^2} + \ln|1 + \sqrt{1+1^2}| \right)",
                font_size=36,
            )
            .next_to(line9, DOWN, buff=0.5)
            .shift(LEFT * 1)
        ).next_to(line9, DOWN)

        self.play(
            TransformMatchingTex(
                line9,
                L_sub_1_target,
                key_map={
                    r"\left[": r"",
                    r"\right]_{0}^{1}": r"",
                    r"x \sqrt{1+x^2} + \ln|x + \sqrt{1+x^2}|": r"1 \sqrt{1+1^2} + \ln|1 + \sqrt{1+1^2}|",
                },
            ),
            run_time=2,
        )
        self.play(L_sub_1_target.animate.to_edge(UP))
        self.wait(1)

        L_sub_0 = MathTex(
            r"-",
            r"\frac{1}{2} \left( 0 \sqrt{1+0^2} + \ln|0 + \sqrt{1+0^2}| \right)",
            font_size=36,
        ).next_to(L_sub_1_target, DOWN)
        self.play(Write(L_sub_0[0]), Write(L_sub_0[1]))
        self.wait(1)

        L_result_1 = MathTex(
            r"=", r"\frac{1}{2} \left( \sqrt{2} + \ln|1 + \sqrt{2}| \right)"
        ).next_to(L_sub_0, DOWN)
        L_result_0 = MathTex(r" + 0").next_to(L_result_1, RIGHT)
        L_result = MathTex(r"\approx 1.147793", font_size=40).next_to(L_result_1, DOWN)

        self.play(
            TransformFromCopy(L_sub_1_target, L_result_1),
            L_sub_1_target.animate.set_color(RED),
        )
        self.play(L_sub_1_target.animate.set_color(WHITE))
        self.play(
            TransformFromCopy(L_sub_0, L_result_0), L_sub_0.animate.set_color(RED)
        )
        self.play(L_sub_0.animate.set_color(WHITE))
        self.wait(1)
        self.play(Write(L_result))
        self.wait(2)

        # Re-visualize
        self.play(FadeOut(*self.mobjects))
        RES = MathTex(r"L \approx 1.147793", font_size=36).next_to(FuncHighlight, RIGHT)

        FuncHighlight, _ = self.Func_ANIMATE(color=WHITE)
        self.play(FadeIn(VGroup(Axis, axisLabel)))
        self.play(DrawBorderThenFill(Func), run_time=2)
        self.wait(0.5)
        self.play(Write(funcLabel))
        self.play(Create(VGroup(pointA, pointB, pointALabel, pointBLabel)), run_time=2)
        self.wait(1)
        self.play(Create(FuncHighlight), run_time=3)
        self.play(Write(RES))

        self.wait()
