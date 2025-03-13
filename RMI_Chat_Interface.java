import java.rmi.Remote;
import java.rmi.RemoteException;

public interface RMI_Chat_Interface extends Remote {
    void sendToServer(String message) throws RemoteException;
}
