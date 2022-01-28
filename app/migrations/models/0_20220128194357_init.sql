-- upgrade --
CREATE TABLE IF NOT EXISTS "admin" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "password" VARCHAR(200) NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "username" VARCHAR(30) NOT NULL UNIQUE,
    "email" VARCHAR(50) NOT NULL UNIQUE,
    "nickname" VARCHAR(30) NOT NULL,
    "hashed_password" VARCHAR(200) NOT NULL,
    "is_verified" BOOL NOT NULL  DEFAULT False,
    "is_active" BOOL NOT NULL  DEFAULT False,
    "registered_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "todo" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "title" VARCHAR(200) NOT NULL,
    "due_date" DATE NOT NULL,
    "is_done" BOOL NOT NULL  DEFAULT False,
    "creator_id" UUID NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "user_user" (
    "user_rel_id" UUID NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    "user_id" UUID NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
