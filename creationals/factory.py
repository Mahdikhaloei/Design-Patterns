"""
    Factory:
        Is a creational design pattern that provides an interface for creating objects in a superclass,
        but allows subclasses to alter the type of objects that will be created.
"""

from abc import ABC, abstractmethod
import subprocess
import shutil


class Database(ABC):
        
    @abstractmethod
    def backup(self):
        pass
    
    def call_run_backup(self, **kwargs):
        product = self.backup()
        result = product.run_backup(**kwargs)
        return result


class PostgresBackup(Database):
    def backup(self):
        return Postgres()


class SqliteBackup(Database):
    def backup(self):
        return Sqlite()


class Postgres:    
    def run_backup(self, **kwargs):
        db_name = kwargs.get("db_name", "database_name")
        db_user = kwargs.get("db_user", "database_user")
        db_host = kwargs.get("db_host", "database_host")
        backup_file = kwargs.get("backup_file", './backup/postgres_backup.sql')
        
        try:
            subprocess.run(['pg_dump', '-U', db_user, '-h', db_host, '-f', backup_file, db_name])
            print(f"PostgreSQL backup successfully created at {backup_file}")
        except Exception as e:
            print(f"PostgreSQL backup failed: {e}")
        

class Sqlite:
    def run_backup(self, **kwargs):
        db_file = kwargs.get("db_file", "/path/to/your/database.db")
        backup_file = kwargs.get("backup_file", './backup/backup.sql')
        
        try:
            shutil.copy2(db_file, backup_file)
            print(f"SQLite backup successfully created at {backup_file}")
        except Exception as e:
            print(f"SQLite backup failed: {e}")



def client(db_type, **kwargs):
    databases = {
        "postgres": PostgresBackup,
        "sqlite": SqliteBackup
    }
    result = databases[db_type]().call_run_backup(**kwargs)
    return result

db_info = {
    "db_name": "test",
    "db_user": "mahdikhaloei",
    "db_host": "localhost",
}

# Running
client("postgres", **db_info)
