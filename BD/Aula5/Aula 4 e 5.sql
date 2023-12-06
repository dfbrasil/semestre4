/*CREATE TABLE IF NOT EXISTS Aluno(
	matricula_aluno INT NOT NULL,
	nome VARCHAR(20) NOT NULL,
	sobrenome VARCHAR(20) NOT NULL,
	idade INT,
	sexo CHAR(1)
);

CREATE TABLE IF NOT EXISTS Turma(
	id_turma INT NOT NULL,
	nome_turma VARCHAR(20) NOT NULL
);*/

/*ALTER TABLE aluno
ADD id_turma INT;*/

/*ALTER TABLE Turma
ADD CONSTRAINT pk_turma
PRIMARY KEY (nome_turma);*/

/*ALTER TABLE Turma
ADD CONSTRAINT u_turma
UNIQUE (id_turma);*/

/*ALTER TABLE Aluno
ADD CONSTRAINT fk_turma
FOREIGN KEY (id_turma) REFERENCES Turma(id_turma);*/

/*INSERT INTO Turma(id_turma, nome_turma)
VALUES (1, 'Turma 1');

INSERT INTO Aluno(matricula_aluno, nome, sobrenome, idade, sexo, id_turma)
VALUES(1234, 'Daniel', 'Freitas', 40, 'M', 1);

INSERT INTO Aluno(matricula_aluno, nome, sobrenome, idade, sexo, id_turma)
VALUES(56789, 'Daniel', 'Brasil', 41, 'M', 1);*/

--SELECT nome FROM Aluno WHERE nome='Daniel';

--SELECT * FROM Aluno WHERE sexo='M';

--SELECT sobrenome FROM Aluno WHERE sexo='M';
