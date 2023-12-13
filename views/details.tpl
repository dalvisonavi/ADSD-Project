<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
}
</style>
</head>
<body>
<h2> Orders <h2>
<hr/>
<table style="width:100%">
 <tr>
    <th style="text-align:left">Order Number </th> 
    <th style="text-align:left">Quantity</th> 
    <th style="text-align:left"> Cake type </th> 
    <th style="text-align:left"> Operation</th>
  </tr>
% for details in shopping_list:
  <tr>
    <td>{{str(details['orderNumber'])}}</td>
    <td>{{str(details['quantity'])}}</td>
    </th><td><{{details['cakeType']}}</td>
    <td><a href="/delete/{{str(details['orderNumber'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
</body>
</html>