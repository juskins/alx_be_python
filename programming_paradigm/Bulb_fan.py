class Device:
   def __init__(self,name,is_on):
      self.name=name
      self.is_on=is_on
      self.turned_on=False
   def turn_on(self):
      if not self.turned_on:
         self.turned_on=True
         return (f"{self.name} is now ON.")
      else:
         return (f"{self.name} is already ON.")
   def turn_off(self):
      if self.turned_on:
         self.turned_on=False
         return (f"{self.name} is now OFF.")
      else:
         return (f"{self.name} is already OFF.")
      

class SmartBulb(Device):
   """A smart bulb device with adjustable brightness."""
   def __init__(self, name, is_on, brightness=0):
      super().__init__(name, is_on)
      self.brightness = brightness  # 0-100
   
   def set_brightness(self, level):
      """Set the brightness level (0-100)."""
      if 0 <= level <= 100:
         self.brightness = level
         return f"{self.name} brightness set to {level}%."
      else:
         return "Brightness must be between 0 and 100."


class SmartFan(Device):
   """A smart fan device with adjustable speed."""
   def __init__(self, name, is_on, speed=1):
      super().__init__(name, is_on)
      self.speed = speed  # 1-5
   
   def set_speed(self, level):
      """Set the fan speed (1-5)."""
      if 1 <= level <= 5:
         self.speed = level
         return f"{self.name} speed set to {level}."
      else:
         return "Speed must be between 1 and 5."
   
   
# Example usage:
bulb = SmartBulb("Living Room Bulb", False)
print(bulb.turn_on())
print(bulb.set_brightness(75))
print(bulb.turn_off())

fan = SmartFan("Bedroom Fan", False)
print(fan.turn_on())
print(fan.set_speed(3))
print(fan.turn_off())