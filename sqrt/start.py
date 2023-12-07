# 手动开方动画
# 从手动开方到牛顿迭代方程
from manimlib import *

class SqrtByHand(Scene):
    def construct(self):
        introText = Text('所以，如何手动开平方？', font='Source Han Sans')
        quizText = Text('例：如何求根号 6？', font='Source Han Sans')
        # 所以，如何手动求平方根？
        self.play(ShowCreation(introText))
        self.wait(1)
        # 例：如何求根号 6？
        self.play(Transform(introText, quizText), run_time=1)
        self.wait(2)
        self.play(Uncreate(introText), run_time=1)
        self.wait(0.5)
        quizSquareSideLength = np.sqrt(6)
        quizSquare = Square(side_length=quizSquareSideLength, fill_opacity=0.5, fill_color=BLUE)
        quizSquare.center()
        quizSquareLabel = Tex('a = ?')
        quizSquareLabel.next_to(quizSquare, UP)
        sLabel = Tex('S = 6', font_size=40)
        # 这就好像我有一个面积为 6 的正方形，现在，我想知道它的边长是多少
        self.play(FadeIn(quizSquare), Write(sLabel))
        self.wait(1)
        self.play(Write(quizSquareLabel))
        self.wait(2)
        tryLabel = Tex('\\sqrt{{6}} = ?')
        tryLabel.next_to(quizSquare, UP)
        # 如果他的面积为一个完全平方数，比如9，我可以很容易求到他的边长，即根号 9，它等于 3
        # 但是，6 显然不是一个完全平方数，根号 6 的值我们也无法轻易得到
        self.play(Transform(quizSquareLabel, tryLabel))
        self.wait(1)
        self.play(Uncreate(quizSquareLabel), Uncreate(sLabel))
        self.wait(1)
        # 我们不妨从面积同样为 6，但邻边不相等的长方形看起
        self.play(quizSquare.animate.stretch(1.5, dim=0))
        self.play(quizSquare.animate.stretch(1/1.5, dim=1))
        # 假设这个长方形长为 L，
        self.wait(1)
        bBrace = BraceLabel(
            obj=quizSquare,
            text='L',
            brace_direction=DOWN
        )
        lBrace = BraceLabel(
            obj=quizSquare,
            text='\\frac{S}{L}',
            brace_direction=LEFT
        )
        self.add(bBrace)
        self.play(ShowCreation(bBrace))
        self.wait(1)
        # 那么他的宽就等于面积 S 除以长 L
        self.add(lBrace)
        self.play(ShowCreation(lBrace))
        # 现在的问题变为，如何画出那个长和宽无限接近的 "正方形"
        # 很自然地想到，根号 S 应该是一个介于长和宽之间的值
        quizGroup1 = VGroup()
        quizGroup1.add(quizSquare, lBrace, bBrace)
        # self.play(quizGroup.animate.scale(0.9).to_corner(UR, buff=1))
        self.play(quizGroup1.animate.to_edge(UP, buff=1))
        self.wait(1)
        # 把长和宽的一般作为新的长，即 L’ = xxxx
        newLTex = Tex('L_{1} = \\frac{1}{2} \cdot (L + \\frac{S}{L})')
        newLTex.scale(0.75).next_to(quizGroup1, DOWN)
        self.play(ShowCreation(newLTex))
        quizGroup1.add(newLTex)
        self.wait(1)
        self.play(quizGroup1.animate.scale(0.7).to_edge(LEFT, buff=1))

        # 以 L1 作为新的长，那么宽为 S / L1
        square2 = Rectangle(width=((math.sqrt(6)  * 3 / 2) + 6 / (math.sqrt(6)  * 3 / 2)) / 2, height= 6 / (((math.sqrt(6)  * 3 / 2) + 6 / (math.sqrt(6)  * 3 / 2)) / 2), fill_opacity=0.5, fill_color=BLUE)
        square2.center()
        self.add(square2)
        self.play(FadeIn(square2))
        # 标记长宽
        lBrace2 = BraceLabel(
            obj=square2,
            text='L_{1}',
            brace_direction=DOWN
        )
        bBrace2 = BraceLabel(
            obj=square2,
            text='\\frac{S}{L_{1}}',
            brace_direction=LEFT
        )
        self.add(lBrace2)
        self.play(ShowCreation(lBrace2))
        self.wait(1)
        self.add(bBrace2)
        self.play(ShowCreation(bBrace2))
        quizGroup2 = VGroup()
        quizGroup2.add(square2, lBrace2, bBrace2)
        self.play(quizGroup2.animate.to_edge(UP, buff=1))
        newLTex2 = Tex('L_{2} = \\frac{1}{2} \cdot (L_{1} + \\frac{S}{L_{1}})')
        newLTex2.scale(0.75).next_to(quizGroup2, DOWN)
        self.play(ShowCreation(newLTex2))
        quizGroup2.add(newLTex2)
        self.wait(1)
        self.play(quizGroup2.animate.scale(0.7).next_to(quizGroup1, RIGHT, buff=0.5))

        ellipsis = Tex('\\dots')
        ellipsis.next_to(quizGroup2, RIGHT, buff=1)
        self.play(Write(ellipsis))

        square3 = Rectangle(width=(math.sqrt(6) + 6 / math.sqrt(6)) / 2, height= 6 / ((math.sqrt(6) + 6 / math.sqrt(6)) / 2), fill_opacity=0.5, fill_color=BLUE)
        square3.next_to(ellipsis, RIGHT, buff=2)
        self.add(square3)
        self.play(FadeIn(square3))
        # 标记长宽
        lBrace3 = BraceLabel(
            obj=square3,
            text='L_{n}',
            brace_direction=DOWN
        )
        bBrace3 = BraceLabel(
            obj=square3,
            text='\\frac{S}{L_{n}}',
            brace_direction=LEFT
        )
        self.add(lBrace3)
        self.play(ShowCreation(lBrace3))
        self.wait(1)
        self.add(bBrace3)
        self.play(ShowCreation(bBrace3))
        quizGroup3 = VGroup()
        quizGroup3.add(square3, lBrace3, bBrace3)
        # self.play(quizGroup3.animate.to_edge(UP, buff=1))
        newLTex3 = Tex('L_{n+1} = \\frac{1}{2} \cdot (L_{n} + \\frac{S}{L_{n}})')
        newLTex3.scale(0.75).next_to(quizGroup3, DOWN)
        self.play(ShowCreation(newLTex3))
        quizGroup3.add(newLTex3)
        self.wait(1)
        self.play(quizGroup3.animate.scale(0.7).next_to(ellipsis, RIGHT, buff=1))
        self.wait(1)
        # 所以，根号 6 等于？
        newQuiz = Tex('\\sqrt{6} = ?')
        newQuiz.to_edge(DOWN, buff=2)
        self.play(Write(newQuiz))
        self.wait(0.5)
        self.play(newQuiz.animate.scale(3), newQuiz.animate.move_to(ORIGIN), FadeOut(quizGroup1), FadeOut(quizGroup2), FadeOut(quizGroup3), FadeOut(ellipsis))
        self.wait(1)

        equationTex = Tex('L_{n+1} = \\frac{1}{2} \cdot (L_{n} + \\frac{S}{L_{n}})')
        equationTex.center()
        # 把这个问题先放到一边
        self.play(Uncreate(newQuiz))
        self.wait(0.25)
        self.play(Write(equationTex))
        self.wait(1)
        equationTex1 = Tex('L_{n+1} = \\frac{1}{2} \cdot (L_{n} + \\frac{6}{L_{n}})')
        self.play(Transform(equationTex, equationTex1))
        self.wait(1)
        equationTex2 = Tex('L_{1} = \\frac{1}{2} \cdot (3 + \\frac{6}{3})')
        equationTex3 = Tex('L_{1} = \\frac{1}{2} \cdot (3 + \\frac{6}{3}) = 2.5')
        # 我们把求近似边长的过程代入数值, 不妨取第一个 L 值为 3，即 6 的一半，得到第一个近似值 2.5
        self.play(Transform(equationTex, equationTex2))
        self.wait(0.25)
        self.play(Transform(equationTex, equationTex3))
        self.wait(1)
        # 把这个近似值值再次代入作为新的 L，得到第二个近似值
        equationTex4 = Tex('L_{2} = \\frac{1}{2} \cdot (L_{1} + \\frac{6}{L_1})')
        equationTex5 = Tex('L_{2} = \\frac{1}{2} \cdot (2.5 + \\frac{6}{2.5}) = 2.45')
        self.play(Transform(equationTex, equationTex4))
        self.wait(0.25)
        self.play(Transform(equationTex, equationTex5))
        self.wait(1)
        # 我们将通过程序迭代多次，得到 L10
        equationTex6 = Tex('L_{10} = \\frac{1}{2} \cdot (L_{9} + \\frac{6}{L_9}) = 2.449489742783178')
        self.play(Transform(equationTex, equationTex6))
        self.wait(1)
        # 我们来看一下，通过计算器得到的根号 6
        answerTex = Tex('\\sqrt{6} = \\textcolor{red}{2.449489742783178}0981972840747059')
        answerTex.center()
        textTex = Tex('L_{2} = \\frac{1}{2} \cdot (2.5 + \\frac{6}{2.5}) = 2.45')
        textTex.center().shift(DOWN*1)
        self.play(equationTex.animate.shift(UP*1))
        self.play(Write(answerTex))
        self.wait(1)
        self.play(Write(textTex))
        self.wait(1)
        self.play(FadeOut(equationTex), FadeOut(answerTex), FadeOut(textTex))

        # 对任意面积S的正方形求其边长近似值，也等于求方程 x2 - S = 0 的近似解x0
        # 下面是牛顿迭代方程的说明
        # 我们计算函数 fx = x2 - S 在x = x0 处的切线同x轴的交点的x坐标，一般来说，这会是一个更优的近似解
        # 由于该点导数即等于切线斜率，于是得到
        equationTexNewton = Tex('f^{\'}{(x_{0})} = \\frac{f(x_{0}) - 0}{x_{0} - x_{1}}')
        self.play(Write(equationTexNewton))
        self.wait(1)
        # 整理一下得到
        equationTexNewton1 = Tex('x_{0} - x_{1} = \\frac{x^{2}_{0} - S}{2x_{0}}')
        equationTexNewton2 = Tex('x_{1} = \\frac{1}{2} \\cdot (x_{0} + \\frac{S}{x_{0}})')
        self.play(Transform(equationTexNewton, equationTexNewton1))
        self.wait(0.5)
        self.play(Transform(equationTexNewton, equationTexNewton2))
        self.wait(1)
        equationTex1.center()
        self.play(equationTexNewton.animate.shift(UP*2))
        self.play(FadeIn(equationTex1))
        self.wait(1)
        self.play(FadeOut(equationTex1), FadeOut(equationTexNewton))

        # 参考
        title = Text('参考资料', font='Source Han Sans', font_size=40)
        title.to_corner(UL, buff=1)
        refer1 = Text('1. 牛顿法 - 中文维基', font='Source Han Sans', font_size=30)
        refer2 = Text('2. 如何通俗易懂地讲解牛顿迭代法求开方 - 知乎', font='Source Han Sans', font_size=30)
        refer3 = Text('3. 牛顿迭代法 - OIWiki', font='Source Han Sans', font_size=30)
        refer1.next_to(title, DOWN).align_to(title, LEFT)
        refer2.next_to(refer1, DOWN).align_to(refer1, LEFT)
        refer3.next_to(refer2, DOWN).align_to(refer2, LEFT)
        gg = VGroup()
        gg.add(title, refer1, refer2, refer3)
        self.play(ShowCreation(gg))
        self.wait(1)






