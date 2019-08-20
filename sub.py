import maestro
import time
servo = maestro.Controller()
servo.runScriptSub(0)
print("sub0")
time.sleep(3)
servo.runScriptSub(1)
print("sub1")
