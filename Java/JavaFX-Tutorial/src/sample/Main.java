package sample;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;


public class Main extends Application
{


    Stage window;

    @Override
    public void start(Stage window)
    {
      Label label10 = new Label("Hi");
      VBox layout = new VBox(20);
      layout.getChildren().add(label10);
      Scene scene01 = new Scene(label10,200,2000);
      window.setScene(scene01);
      window.showAndWait();



    }

    public static void Main(String[] args) {launch(args);}


}
