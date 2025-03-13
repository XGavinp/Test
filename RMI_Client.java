import java.rmi.Naming;
import java.util.Scanner;

public class RMI_Client {
    public static void main(String[] args) {
        try {
            // Look up the remote object from the registry on port 6000
            RMI_Chat_Interface chatServer = (RMI_Chat_Interface) Naming.lookup("//localhost:6000/chat");

            // Create a Scanner to read input from the console
            Scanner scanner = new Scanner(System.in);
            String message;

            System.out.println("Enter message to send to the server (type 'exit' to quit):");

            // Continuously read and send messages to the server
            while (!(message = scanner.nextLine()).equalsIgnoreCase("exit")) {
                chatServer.sendToServer(message);
                System.out.println("Message sent to server: " + message);
            }

            scanner.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
