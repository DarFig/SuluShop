CREATE database IF NOT EXISTS sulushop;
	use sulushop;

CREATE TABLE IF NOT EXISTS usuario(
  id int unsigned AUTO_INCREMENT PRIMARY key,
  nombre varchar(140) NOT null,
  apellidos varchar(140) not null,
  fecha_nacimiento date not null,
  direccion varchar(140) not null,
  email varchar(140) not null,
  telefono varchar(20) not null,
  contrasena varchar(300) not null,
  imagen varchar(140)
);

CREATE TABLE IF NOT EXISTS producto(
  id int unsigned AUTO_INCREMENT PRIMARY key,
  nombre varchar(140) not null,
  precio double not null,
  puntuacion double,
  descripcion varchar(500) not null,
  detalles varchar(1500) not null,
  stock boolean not null
);

CREATE TABLE IF NOT EXISTS foto(
	id int unsigned primary key auto_increment,
  url varchar(140) not null,
  principal boolean,
);

CREATE TABLE IF NOT EXISTS foto_producto(
	id int unsigned primary key auto_increment,
	id_foto int unsigned,
	index (id_foto),
	foreign key (id_foto)
		references img (id)
		on delete cascade on update no action,
	id_producto int unsigned,
	index (id_producto),
	foreign key (id_producto)
		references post (id)
		on delete cascade on update no action
);
