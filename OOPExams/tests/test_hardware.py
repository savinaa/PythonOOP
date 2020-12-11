import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self) -> None:
        self.hardware=Hardware("SSD", "Light", 1000, 1000)

    def test_init(self):
        self.assertEqual("SSD",self.hardware.name)
        self.assertEqual("Light",self.hardware.type)
        self.assertEqual(1000,self.hardware.capacity)
        self.assertEqual(1000,self.hardware.memory)

    def test_install(self):
        self.assertEqual([],self.hardware.software_components)
        software=Software("Mozilla","browser", 200, 200)
        self.hardware.install(software)
        self.assertEqual([software],self.hardware.software_components)

    def test_install_raises_error(self):
        with self.assertRaises(Exception) as e:
            software1 = Software("Ciberpunk 2077", "game", 2000, 500)
            self.hardware.install(software1)
        self.assertEqual("Software cannot be installed", str(e.exception))

    def test_uninstall(self):
        software = Software("Mozilla", "browser", 200, 200)
        self.hardware.install(software)
        self.hardware.uninstall(software)
        self.assertEqual([], self.hardware.software_components)
