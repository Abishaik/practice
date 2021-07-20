
public class TecAdminSeleniumTest {
 
        public static void main(String[] args) {
                System.setProperty("webdriver.chrome.driver", "\\usr\\bin\\chromedriver");
 
                WebDriver driver = new ChromeDriver();
 
                driver.get("https://google.com");
 
                Thread.sleep(1000);
 
                driver.quit();
        }
}