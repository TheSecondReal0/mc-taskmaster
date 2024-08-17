CREATE TABLE players (
    id UUID PRIMARY KEY,
    discord_id BIGINT NOT NULL
);

CREATE TABLE categories (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE player_categories_xref (
    player_id UUID NOT NULL REFERENCES players (id),
    category_id UUID NOT NULL REFERENCES categories (id),
    PRIMARY KEY (player_id, category_id)
);

CREATE TABLE seasons (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    session INT NOT NULL,
    start TIMESTAMP,
    end TIMESTAMP
);

CREATE TABLE player_season (
    player_id UUID NOT NULL REFERENCES players (id),
    season INT NOT NULL REFERENCES season(id),
    score BIGINT
)

CREATE TABLE tasks (
    id UUID NOT NULL,
    season INT NOT NULL REFERENCES seasons (id),
    name VARCHAR(255) UNIQUE NOT NULL, -- unique name of the task, necessary?
    description TEXT NOT NULL,
    points INT,
    min_session INT,
    max_session INT,
    PRIMARY KEY (id, season)
);

CREATE TABLE task_categories_xref (
    task_id UUID NOT NULL REFERENCES tasks (id),
    category_id UUID NOT NULL REFERENCES categories (id),
    PRIMARY KEY (task_id, category_id)
);

CREATE TABLE player_tasks (
    player_id UUID NOT NULL REFERENCES players (id),
    task_id UUID NOT NULL REFERENCES tasks (id),
    session INT NOT NULL,
    time_assigned TIMESTAMP NOT NULL,
    PRIMARY KEY (player_id, task_id)
);

CREATE TABLE player_tasks_completed (
    player_id UUID NOT NULL REFERENCES players (id),
    task_id UUID NOT NULL REFERENCES tasks (id),
    session INT NOT NULL,
    time_completed TIMESTAMP NOT NULL,
    PRIMARY KEY (player_id, task_id)
);

CREATE TABLE player_tasks_failed (
    player_id UUID NOT NULL REFERENCES players (id),
    task_id UUID NOT NULL REFERENCES tasks (id),
    session INT NOT NULL,
    time_failed TIMESTAMP NOT NULL,
    PRIMARY KEY (player_id, task_id)
);