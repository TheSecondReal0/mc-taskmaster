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

CREATE TABLE season (
    name TEXT NOT NULL,
    session INT NOT NULL,
    start TIMESTAMP,
    end TIMESTAMP
);

CREATE TABLE player_season_xref (
    player_id UUID NOT NULL REFERENCES players (id),
    season INT NOT NULL REFERENCES season(id),
    score BIGINT
)

CREATE TABLE tasks (
    id UUID PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL, -- unique name of the task, necessary?
    description TEXT NOT NULL,
    points INT,
    min_session INT,
    max_session INT
);

CREATE TABLE task_categories_xref (
    task_id UUID NOT NULL REFERENCES tasks (id),
    category_id UUID NOT NULL REFERENCES categories (id),
    PRIMARY KEY (task_id, category_id)
);

CREATE TABLE player_tasks_xref (
    player_id UUID NOT NULL REFERENCES players (id),
    task_id UUID NOT NULL REFERENCES tasks (id),
    session_assigned INT NOT NULL,
    time_assigned TIMESTAMP NOT NULL,
    session_resolved INT,
    time_resolved TIMESTAMP,
    status VARCHAR(255) NOT NULL CHECK status IN ('assigned', 'failed', 'completed'),
    PRIMARY KEY (player_id, task_id, session_assigned)
);
