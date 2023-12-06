<html>
<body>
<h2>Products List</h2>
<hr/>
<table>
% for product in product_list:
  <tr>
  <td>{{str(product['ProductName'])}}</td>
  <td><a href="/update/{{str(product['id'])}}">update</a></td>
  <td><a href="/delete/{{str(product['id'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<a href="/add">Add a new Product</a>
<hr/>
</body>
</html>