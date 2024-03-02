import {drizzle} from 'drizzle-orm/bun-sqlite';
import {Database} from 'bun:sqlite';
import {publicProcedure, router} from "./server/trcp";
import {createHTTPServer} from "@trpc/server/adapters/standalone";
import cors from 'cors';
import {contracts} from "./schema";
import {z} from 'zod'

const sqlite = new Database('../Data/Contratos.sqlite');
const db = drizzle(sqlite);

const appRouter = router({
    contractList: publicProcedure.input(z.object({
        PageSize: z.number().min(1).max(99),
        PageCount: z.number().min(0),
    })).query(async (opts) => {
        const {input} = opts;

        return db.select()
            .from(contracts)
            .limit(input.PageSize)
            .offset(input.PageCount * input.PageSize);
    }),
});

const server = createHTTPServer({
    router: appRouter,
    middleware: cors(),
})

server.listen(8000);

export type AppRouter = typeof appRouter;