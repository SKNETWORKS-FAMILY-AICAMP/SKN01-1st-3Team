CREATE TABLE `car` (
	`id` INT(10) NOT NULL AUTO_INCREMENT,
	`모델명` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`차량한줄설명` VARCHAR(100) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`일회충전주행가능거리` VARCHAR(100) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`충전시간` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`최고출력` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`전장` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`전폭` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`전고` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`축거` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	PRIMARY KEY (`id`) USING BTREE
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=189
;
