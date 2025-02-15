import {SerialUSB} from './serialusb.js';
import * as due from './duelink.js';

let duedemo = new due.DUELinkController(new SerialUSB());
await duedemo.Connect();

async function demo() {
    // for (let i = 0; i < 5; i++) {
    //     await duedemo.Digital.Write(duedemo.Pin.Led, true);
    //     await duedemo.System.Wait(200);
    //     await duedemo.Digital.Write(duedemo.Pin.Led, false);
    //     await duedemo.System.Wait(200);
    // }

    // for (let i = 0; i < 10; i++) {
    //     await duedemo.System.Println("Line-" + i);
    // }

    await duedemo.System.Println("test");

    let nameList = ["Bob","Lisa","Gus","Tina"];

    for(const name of nameList) {
        await duedemo.System.Println(name);
    }

    // let x = 64;
    // let y = 32;
    // let dx = 3;
    // let dy = 2;

    // duedemo.Button.Enable('A',1);
    // for(;;) {
    //     await duedemo.Display.Clear(0);
    //     await duedemo.Display.DrawCircle(1,x,y,3);
    //     await duedemo.Display.Show();
    //     x+=dx;
    //     y+=dy;
    //     if (x < 0 || x > 128) dx = -dx;
    //     if (y < 0 || y > 64) dy = -dy;
    //     if (await duedemo.Button.WasPressed('A')) console.log("Pressed")
    //     if (await duedemo.Touch.Read(0)) console.log("Touch");
    // }
}

await demo();

//close serial com
await duedemo.Disconnect()

console.log("The End!");