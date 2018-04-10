<?php 

    include '../includes/header.php'; 

    $handle = fopen("../data/buildlist.txt", "r");
    // Header
    $line = fgets($handle);

    $datearray  = explode("|", $line);
    $month = $datearray[0];
    $day   = $datearray[1];
    
 ?>

<form action="buildMailer.php" method="POST">
    <table border="0" width="1000"  height='450'  style="background-color: #FFFFFF;">
        <tr>
        <td width='400'  valign="top" >
            <table border="0" width='300' height='640' valign="top"  style="background-color: lightgray;">
               <tr>
                      <td colspan="2" valign="bottom" height='75' style="background-color: #FFFFFF;"> 
                         
                     </td>
                </tr>   
               <tr>
                      <td colspan="2" id="right_pane_title" align="center" valign="center" > 
                          <b>Build Mailer List</b>
                     </td>
                </tr>   
                <tr  id="nav_tr" >
                     <td width='20%' height='5' align="center"> 
                         <img src="../images/CreditCard.gif" width="40px" height="40px" alt="AddCreditor"/>
                     </td>
                     <td width='80%' id="nav_td" > 
                         &nbsp;&nbsp;Foreclosure Mailer
                     </td>
                </tr>   
               <tr >
                      <td colspan="2" height="150" align="center" valign="center" > 
      
                     </td>
                </tr>   

                <tr>
                     <td width='20%' height='120' align="center" > 
                     </td>
                     <td width='80%' style="font-family: Times New Roman; font-size: 18px;" > 
                         <br><br><br>
                     </td>
                </tr>   
                <tr>
                     <td width='20%' height='120' align="center" > 
                     </td>
                     <td width='80%' style="font-family: Times New Roman; font-size: 18px;" > 
                         <br><br><br>
                     </td>
                </tr>   
             </table>
        </td>  
        <td height="50">
            &nbsp;
        </td>
        <td align="left" valign='top' style="background-color: white;" >
   
            <div align="center" style="font-size: 30px; font-family: Times New Roman; color: #660000">
                <br>List of Foreclosures - <?php echo $month . ' ' .  $day; ?> Sale date
            </div>

            <table border="0" id="listformtable">
               <tbody>
               <tr>
                   <td colspan="5">
                       &nbsp;
                   </td>
               </tr>                    
               <tr>
                   <td colspan="5" align="center">            
                       <h1 id="login_h1"><B>Create Foreclosure Mailer</B></h1>
                       <input type="hidden" name="Month" value="<?php echo $month; ?>" />
                       <input type="hidden" name="Day" value="<?php echo $day; ?>" />
                   </td>
               </tr>
                <tr>
                    <td align="left" height="30" valign="center" style="color: #660000; font-family: Times New Roman; font-size: 18px">
                        <b>&nbsp;&nbsp;Company</b>
                    </td>
                    <td align="left" height="30" valign="center" style="color: #660000; font-family: Times New Roman; font-size: 18px">
                        <b>Business type</b>
                    </td>
                    <td align="left" height="30" valign="center" style="color: #660000; font-family: Times New Roman; font-size: 18px">
                        <b>Records #</b>
                    </td>
               </tr>
               
               <?php
                    $i = 0;
                    $total = 0;
                    if ($handle) {
                       while (($line = fgets($handle)) !== false) {
                            $list = explode("|", $line);
                            $result = count($list);
                            if ($result > 1) {
                                $company   = $list[0];
                                $type      = $list[1];
                                $buildfile = $list[2];
                                $records   = $list[3];
                            } else {
                                $duplicates = $list[0];
                                $total_dupls = $total - $duplicates;
                                break;
                            }                 
                            $total = $total + $list[3];
                            $i = $i + 1;
                ?>
                    <tr>
                        <td width="40%" height="27px" align="left" valign="center" 
                            style="background-color: white; font-family: Times New Roman; font-size: 18px">
                            &nbsp;&nbsp;<a href="<?php echo $url; ?>" style="color: #660000"><?php echo $company; ?></a>
                        </td>
                        <td width="22%" height="27px" align="left" valign="center" 
                            style="background-color: white; font-family: Times New Roman; font-size: 18px">
                           <?php echo $type; ?>
                        </td>
                        <td width="10%" height="27px" align="right" valign="center" 
                            style="background-color: white; font-family: Times New Roman; font-size: 18px">
                           <?php echo $records; ?> &nbsp;
                            <input type="hidden" name="buildfile<?php echo $i; ?>" value="<?php echo $buildfile;?>" />
                        </td>
                    </tr>
                <?php  } ?>                
                        <td colspan="2" height="27px" align="left" style="background-color: white;"> 
                            <b>Sub total of records</b>
                        </td>
                        <td height="27px" align="right" style="background-color: white;"> 
                            <b><?php echo $total; ?> &nbsp;</b>
                        </td>
                   </tr>
                    <tr>
                        <td colspan="2" height="27px" align="left" style="background-color: white;"> 
                            Total # of duplicates removed
                        </td>
                        <td height="27px" align="right" style="background-color: white;"> 
                            -<?php echo $duplicates; ?> &nbsp;
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2" height="27px" align="left" style="background-color: white;"> 
                            <b>Total # of records</b>
                        </td>
                        <td height="27px" align="right" style="background-color: white;"> 
                            <b><?php echo $total_dupls; }?> &nbsp;</b>
                        </td>
                   </tr>
           </tbody>
           <br>
           <tr>
                <td align="left" colspan='5' height="60" align="center" valign="top" 
                   style="font-family: Times New Roman; font-size: 20px;" >
                   <br>
                   <input type="button" value="BACK" 
                   onclick="window.location.href='javascript:history.back()'"                          
                   style="color: white; height: 35px; width: 100px;"
                   id="frmButton" />
                   &nbsp; &nbsp;
                   <input type="submit" value="DOWNLOAD MAILER" 
                          style="color: white; height: 35px; width: 150px;"
                          id="frmButton" />
                   <br>
                   <br>
                </td>
            </tr>
        </table>
       <br><br><br>
    </td>
    </tr>
    </table> 
    </form>
    &nbsp;&nbsp;
    </body>
</html>