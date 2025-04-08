// Conexão com o MongoDB
const { MongoClient } = require('mongodb');

async function initializeDatabase() {
    const uri = "mongodb://localhost:27017"; // Substitua pelo URI do seu MongoDB
    const client = new MongoClient(uri);

    try {
        await client.connect();
        console.log("Conectado ao MongoDB");

        const db = client.db("octofit_db");

        // Criar coleções
        await db.createCollection("users");
        await db.createCollection("teams");
        await db.createCollection("activity");
        await db.createCollection("leaderboard");
        await db.createCollection("workouts");

        // Criar índice único para a coleção 'users'
        await db.collection("users").createIndex({ email: 1 }, { unique: true });
        console.log("Índice único criado para a coleção 'users'");

        // Listar coleções no banco de dados
        const collections = await db.listCollections().toArray();
        console.log("Coleções no banco de dados 'octofit_db':");
        collections.forEach(col => console.log(col.name));
    } catch (error) {
        console.error("Erro ao inicializar o banco de dados:", error);
    } finally {
        await client.close();
    }
}

initializeDatabase();
