
class Test {
    public static void main(String[] args) {
    System.setProperty("Webdriver.chrome.driver","\\home\\abi\\Downloads\\chromedriver_linux64");
    Webdriver driver = new ChromeDriver();
    driver.manage.maximize();
    driver.get("https://github.com/");
    
    }
}