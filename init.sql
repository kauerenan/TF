CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
);

INSERT INTO alunos (nome, idade) VALUES
('Alice', 22),
('Bruno', 24),
('Carla', 21);
