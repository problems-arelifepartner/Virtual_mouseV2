# Virtual_mouseV2
Human mouse 


1. Authorize root to use the graphical display (Run this BEFORE switching to root)


``` xhost +SI:localuser:root ```

2. Switch to your root terminal environment


``` sudo -i ```

3. Navigate into your project repository 


``` cd /path/to/your/ai-virtual-mouse ```

4. Activate the virtual environment


``` source venv/bin/activate ```

5. Run the script while explicitly declaring the local hardware display


``` DISPLAY=:0 python3 main.py ```



``` sudo apt-get update && sudo apt-get install -y python3-tk scrot ```

