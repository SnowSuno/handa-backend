-- upgrade --
ALTER TABLE "user" ADD "desc" TEXT NOT NULL  DEFAULT '';
-- downgrade --
ALTER TABLE "user" DROP COLUMN "desc";
