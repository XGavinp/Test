import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class RMI_Server extends UnicastRemoteObject implements RMI_Chat_Interface {
    public RMI_Server() throws RemoteException {
        super();
    }

    @Override
    public void sendToServer(String message) throws RemoteException {
        System.out.println("Client says: " + message);
    }

    public static void main(String[] args) throws Exception {
        // Create the RMI registry on port 6000
        Registry rmiregistry = LocateRegistry.createRegistry(6000);
        
        // Bind the RMI Server object to the registry under the name 'chat'
        rmiregistry.bind("chat", new RMI_Server());
        
        System.out.println("Chat server is running...");
    }
}
