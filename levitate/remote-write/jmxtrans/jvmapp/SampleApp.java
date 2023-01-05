public final class SampleApp {
  public static void main(String []args) throws Exception {
    final java.util.Random generator = new java.util.Random();
    while (true) {
      System.out.println("test");
      generator.ints(1000000, 0, 100).sorted();
      Thread.sleep(5000L);
    }
  }
}
