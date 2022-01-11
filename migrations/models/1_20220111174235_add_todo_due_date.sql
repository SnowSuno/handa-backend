-- upgrade --
ALTER TABLE "todo" ADD "due_date" DATE NOT NULL;
-- downgrade --
ALTER TABLE "todo" DROP COLUMN "due_date";
