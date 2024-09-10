-- DROP TABLE IF EXISTS "Todo";


-- CREATE TABLE "Todo" (
--   "id" SERIAL PRIMARY KEY,
--   "title" varchar NOT NULL,
--   "description" varchar,
--   "due_date" timestamp,
--   "created_at" timestamp DEFAULT (now()),
--   "priority" varchar DEFAULT 'High',
--   "completed" bool DEFAULT false
-- );


-- INSERT INTO "Todo" ("title", "description", "due_date", "priority", "completed")
-- VALUES
--   ('Buy groceries', 'Buy milk, eggs, and bread', '2024-09-10 12:00:00', 'Medium', false),
--   ('Finish project report', 'Complete the final draft of the report', '2024-09-15 17:00:00', 'High', false),
--   ('Book flight tickets', 'Book tickets for vacation', '2024-09-20 10:00:00', 'Low', false),
--   ('Clean the house', 'Vacuum and mop the floors', '2024-09-07 09:00:00', 'Medium', true),
--   ('Call mom', 'Catch up with mom over the phone', '2024-09-06 18:00:00', 'High', false);




SELECT * FROM "Todo";