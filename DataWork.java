// set CLASSPATH=.;mysql-connector-java-8.0.15.jar

import java.sql.*; 

import java.util.*; 

 

public class DataWork{ 

 

 public static void main(String[] args) { 

//Perform the CRUD create, read, update, delete records with the database 

readAllSQL();

//put C:\mysql-connector-java-8.0.15.jar into Advanced System settings and add an enviornment variable and value;

//chnage the line Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/School","root","q7:?A!c5tZW$./,N"); change DriverManager to SchoolManager

//readByIdSQL(1000); 

//Student stud = new Student("Oakes", "Jill", 3.0, 20, 80); 

//createSQL(1005, stud); 

//updateSQL(1004, stud); 

//deleteSQL(1005); 

//readAllSQL(); 

   }  

 

 private static void readAllSQL(){ 

    ArrayList<Student> studs = new ArrayList<Student>(); 

     try{ 

       //here School is database name, root is username and password
       
       Class.forName("com.mysql.cj.jdbc.Driver");  

       Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/School","root","q7:?A!c5tZW$./,N"); 

         Statement stmt=con.createStatement(); 

         ResultSet rs=stmt.executeQuery("select * from tblStudents"); 

         while(rs.next()){ 

  Student stud = new Student(rs.getString("fldLName"), rs.getString("fldFName"),

rs.getDouble("fldGPA"), rs.getInt("fldCurrentCredits"), rs.getInt("fldTotalCredits")); 

studs.add(stud); 

         } 

      for (Student stud : studs){ 

        System.out.println(stud.getfName() + " " + stud.getlName() + " " + stud.getGPA()); 

      }  

      }catch(Exception e){ System.out.println(e);} 

  } 

} 