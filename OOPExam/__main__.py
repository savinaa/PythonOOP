# you can test your code here
from OOPExam.project.easter_shop import EasterShop
from OOPExam.project.factory.chocolate_factory import ChocolateFactory
from OOPExam.project.factory.egg_factory import EggFactory
from OOPExam.project.factory.paint_factory import PaintFactory

chocolate_factory=ChocolateFactory('chok', 15)
egg_factory=EggFactory('egg', 15)
paint_factory=PaintFactory('paint', 15)
shop=EasterShop('shop',chocolate_factory,egg_factory,paint_factory)
chocolate_factory.add_ingredient('white chocolate',7)
egg_factory.add_ingredient('chicken egg',1)
paint_factory.add_ingredient('red',1)