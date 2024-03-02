import {drizzle} from 'drizzle-orm/bun-sqlite';
import {Database} from 'bun:sqlite';
import {publicProcedure, router} from "./server/trcp";
import {createHTTPServer} from "@trpc/server/adapters/standalone";
import cors from 'cors';
import {contracts} from "./schema";

const sqlite = new Database('../Data/Contratos.sqlite');
const db = drizzle(sqlite);

const appRouter = router({
    contractList: publicProcedure.query(async () => {
        return db.select().from(contracts).limit(10);
    }),
});

const server = createHTTPServer({
    router: appRouter,
    middleware: cors(),
})

server.listen(8000);

export type AppRouter = typeof appRouter;