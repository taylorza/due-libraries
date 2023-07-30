from enum import Enum

class ButtonController:   

    def __init__(self, serialPort):
        self.serialPort = serialPort

    def Enable(self, pin, enable: bool) -> bool:
        pin = (ord(pin) if isinstance(pin, str) else pin) & 0xdf
        if pin != 0 and pin != 1 and pin != 2 and pin != 65 and pin != 66:
            raise ValueError("Invalid pin")
    
        cmd = f"btnenable({pin}, {int(enable)})"

        self.serialPort.WriteCommand(cmd)
        res = self.serialPort.ReadRespone()

        return res.success
    
    def WasPressed(self, pin) -> bool:
        pin = (ord(pin) if isinstance(pin, str) else pin) & 0xdf
        if pin != 0 and pin != 1 and pin != 2 and pin != 65 and pin != 66:
            raise ValueError("Invalid pin")
            
        cmd = f"print(btndown({pin}))"

        self.serialPort.WriteCommand(cmd)
        res = self.serialPort.ReadRespone()

        if res.success:
            try:
                return int(res.respone) == 1
            except:
                pass

        return False
    
    def IsReleased(self, pin) -> bool:
        pin = (ord(pin) if isinstance(pin, str) else pin) & 0xdf
        if pin != 0 and pin != 1 and pin != 2 and pin != 65 and pin != 66:
            raise ValueError("Invalid pin")
            
        cmd = f"print(btnup({pin}))"

        self.serialPort.WriteCommand(cmd)
        res = self.serialPort.ReadRespone()

        if res.success:
            try:
                return int(res.respone) == 1
            except:
                pass

        return False   
       
