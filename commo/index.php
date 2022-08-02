<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<title>Kalimati Prices</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto|Varela+Round|Open+Sans">
<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
<style type="text/css">
.bs-example{
margin: 20px;
}
body {
  background-image: url('1.jpg');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: 100% 100%;
}
</style>
</style>
<script type="text/javascript">
$(document).ready(function(){
$('[data-toggle="tooltip"]').tooltip();   
});
</script>
</head>
<body>
<div class="bs-example">
<div class="container">
<div class="row">
<div class="col-md-12">
<div class="page-header clearfix">
<h2 class="pull-left" style="color: #fff; ">Kalimati Prices</h2>
<form action="" method="POST" style="color: #fff; "> 
Date(yyyy-mm-dd): <input type="text" name="date" placeholder="Enter date in yyyy-mm-dd"><br> 
<input type="submit" name="search" value="Search Prices">
</form>
<?php
include_once 'db.php';
$date= $_POST['date'] ?? null;
if (empty($date)) {
    $date= '2017-01-01'; /* tapailechai db ma vako latest date halnu 2021 wala*/
}
$result= mysqli_query($conn,"SELECT * FROM kmarketopendata where Date='$date'");
?>
<?php
if (mysqli_num_rows($result) > 0) {
?>
<table class='table table-bordered table-striped'background="3.jpg">
<tr>
<td>Date</td>
<td>Commodity</td>
<td>Unit</td>
<td>Minimum</td>
<td>Maximum</td>
<td>Average</td>
</tr>
<?php 
$i=0;
while($row = mysqli_fetch_array($result)) {
?>
<tr>
<td><?php echo $row["Date"]; ?></td>
<td><?php echo $row["Commodity"]; ?></td>
<td><?php echo $row["Unit"]; ?></td>
<td><?php echo $row["Minimum"]; ?></td>
<td><?php echo $row["Maximum"]; ?></td>
<td><?php echo $row["Average"]; ?></td>
</tr>
<?php
$i++;
}
?>
</table>
<?php
}
else{
echo "No result found";
}
?>
</div>
</div>        
</div>
</div>
<div>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
&emsp;&emsp;
<a href="logout.php" class="btn btn-danger ml-3">Logout</a>
</div>
</body>
</html>