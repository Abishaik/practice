
// Class  
public class main{
    
    public static void main(String[] args)
    {
        System.out.println("Hello worldd !");
        // Int
        int a=100;
        System.out.println(a);

        // Double
        double f=100.05;
        System.out.println(f);

        // String
        String s="Abishaik";
        System.out.println(s);

        // Character 
        char c='c';
        System.out.println(c);

        // Boolean
        boolean exp=true;
        System.out.println(exp);

        // if else statement
        if(exp)
        {
            System.out.println("exp is true");
        }
        else{
            //something
        }

        // For Loop
        for(int i=0; i<10; i++)
        {
            p("ABISHAIK prints : "+i);
        }

        // While Loop
        while(exp)
        {
            if(exp)
            {
                // Function written below
                p("This works");
                break;
            }
        } 

    }
    // Function
    public static void p(String s)
    {
        System.out.println(s);
    }
}