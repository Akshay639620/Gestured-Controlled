import java.awt.Dimension;
import java.awt.Robot;
import java.awt.Toolkit;
import java.awt.event.InputEvent;
import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class GestureMouse {
    public static void main(String[] args) {
        try {
            Robot robot = new Robot();
            robot.setAutoDelay(0); // Keeps cursor smooth

            Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
            int screenWidth = (int) screenSize.getWidth();
            int screenHeight = (int) screenSize.getHeight();

            int port = 8765;
            DatagramSocket socket = new DatagramSocket(port);
            byte[] buffer = new byte[256];

            boolean isCurrentlyPinching = false;

            System.out.println("Java Pro Client Active.");
            System.out.println("Tracking: Pinky Knuckle");
            System.out.println("Action: Pinch Thumb + Index to Click/Drag");

            while (true) {
                DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
                socket.receive(packet);
                
                String data = new String(packet.getData(), 0, packet.getLength());
                String[] parts = data.split(",");

                // Now expecting exactly 3 parts: X, Y, PinchState
                if (parts.length == 3) {
                    float x = Float.parseFloat(parts[0]);
                    float y = Float.parseFloat(parts[1]);
                    boolean isPinching = Boolean.parseBoolean(parts[2]);

                    int targetX = (int) (x * screenWidth);
                    int targetY = (int) (y * screenHeight);

                    // Move Mouse
                    robot.mouseMove(targetX, targetY);

                    // Handle Click & Drag
                    if (isPinching && !isCurrentlyPinching) {
                        // Fingers touched -> Press and hold mouse
                        robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
                        isCurrentlyPinching = true;
                    } else if (!isPinching && isCurrentlyPinching) {
                        // Fingers separated -> Release mouse
                        robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
                        isCurrentlyPinching = false;
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}