package Java;

import java.io.File;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class Main {
  static Scanner sc = new Scanner(System.in);
  public static void main(String[] args) {
    List<Toy> list = new ArrayList<>();
    boolean isAct = true;

    while (isAct){
      System.out.println("=================================");
      System.out.println("ПРОГРАММА РОЗЫГРЫША ИГРУШЕК\nКакое действие хотите выполнить:\n" +
                         "1. Добавить игрушку\n2. Изменить шанс\n3. Разыграть игрушку\n4. Выход");
      String command = sc.next();
      switch (command){
        case "1":
          Toy newToy = addToy();
          if (newToy.getId() != -1) {
            list.add(newToy);
          }
          break;
        case "2":
          changeLuck(list);
          break;
        case "3":
          if (list.size() != 0) {
            roll(list);
          } else {
            System.out.println("Список пуст\n");
          }
          break;
        case "4":
          isAct = false;
          break;
        default:
          System.out.println("Нет такой команды\n");
          break;
      }
    }
  }

  public static Toy addToy(){
    try {
      System.out.print("Введите id: ");
      long id = sc.nextLong();
      System.out.print("Введите название: ");
      String name = sc.next();
      System.out.print("Введите количество: ");
      int amount = sc.nextInt();
      System.out.print("Введите шанс: ");
      int luck = sc.nextInt();

      if (id < 1 || amount < 1 || luck < 0 || luck > 100) {
        throw new InputMismatchException();
      }

      System.out.println();
      return new Toy(id, name, amount, luck);
    } catch (InputMismatchException e) {
      System.out.println("Введен неверный формат. Повторите команду\n");
    } catch (Exception e) {
      System.out.println("Что-то пошло не так. Повторите команду\n");
    }

    System.out.println();
    return new Toy(-1, "-1", -1, -1);
  }

  public static void changeLuck(List<Toy> list){
    if (list.size() != 0) {
      System.out.println(list.toString());

      try {
        System.out.print("Введите id игрушки: ");
        long id = sc.nextLong();
        System.out.print("Введите процент удачи: ");
        int luck = sc.nextInt();

        for (Toy t : list) {
          if (t.getId() == id) {
            t.setLuck(luck);
          }
        }
      } catch (InputMismatchException e) {
        System.out.println("Введен неверный формат. Повторите команду\n");
      } catch (Exception e) {
        System.out.println("Что-то пошло не так. Повторите команду\n");
      }
    } else {
      System.out.println("Список пуст\n");
    }
  }

  public static void roll(List<Toy> list){
    Random rnd = new Random();
    boolean nextRoll = true;
    int index = 0;

    while (nextRoll) {
      if (index < list.size()){
        if (list.get(index).getLuck() >= rnd.nextInt(1, 101)) {
          System.out.println("=================================");
          System.out.println("Вы выиграли: " + list.get(index).toString());

          saveResult(list.get(index).toString());

          list.get(index).setAmount(list.get(index).getAmount() - 1);

          if (list.get(index).getAmount() <= 0) {
            System.out.println(list.remove(index));
          }

          nextRoll = false;
        }
      } else {
        index = 0;
      }
    }
  }

  public static void saveResult(String s){
    File myFile = new File("toys.txt");

    if (!myFile.exists()){
      try {
        myFile.createNewFile();
      } catch (Exception e) {
        System.out.println("Не удалось создать файл");
      }
    }

    try (FileWriter fw = new FileWriter(myFile, true)) {
      fw.write(s + "\n");
    } catch (Exception e) {
      System.out.println("Не удалось записать в файл");
    }
  }
}