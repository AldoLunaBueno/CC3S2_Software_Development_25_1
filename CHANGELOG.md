# CHANGELOG

549a948 Done  
047c5f5 Refactor agregar_producto: Separate search logic in private method to give more importance to validation in agregar_producto  
9502584 Implement minimum modifications to the method agregar_producto to pass the test  
a79cc5e Solve exercise 9. Add test for agregar_producto that exceeds stock, and the test is red.  
897adad Refactor aplicar_cupon: Add validations, separate it from logic and document with a docstring.  
effda55 Implement minimum method aplicar_cupon() to pass the test  
7f946ac Solve exercise 8. Add test for aplicar_cupon considering a max limit, and the test is red.  
9b04cb0 Refactor calcular_impuestos() with porcentage validations and add documentation  
bf827c1 Implement minimum method calcular_umpuestos() to pass test  
8d743f2 Solve exercise 7. Add test for calcular_impuestos() method, and it's red  
da9e2c9 Solve exercise 6. Add parametrization for test_aplicar_descuento and test_actualizar_cantidad_producto, and also fix a bug in ProductFactory about stock limit interfering with test randomly.  
9b8dd44 Refactor by using fixtures for instantiate a shopping cart o a generic product where appropiate (instead of instantiate them on every test)  
1dc252b Solve exercise 4. Test and implement obtener_items_ordenados() method of Carrito class, by name and price.  
9711e73 Improve agregar_producto() for pass the test about stock limit and add stock attribute to Producto and ProductoFactory  
cf4053c Solve exercise 3. Test agregar_producto() in relation with stock limit of the product to add to the shopping cart  
8995ab1 Implement aplicar_descuento_condicional() method for conditional discount, and pass tests  
614e2f2 Solve exercise 2. Test that conditional discount method is only apply if the condition is satisfied  
82a20c1 Implement Carrito method for empty its items  
4013416 Solve exercise 1. Add test for empty the Carrito object from its items  
5e1b209 Set initial structure  
342bad0 Initial commit  
