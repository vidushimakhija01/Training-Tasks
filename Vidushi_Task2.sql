CREATE TABLE bank_accounts (
  account_id INT,
  account_holder VARCHAR(50),
  balance NUMERIC(12, 2)
);
INSERT INTO bank_accounts (account_id, account_holder, balance) VALUES
(1, 'Ravi', 10000.00),
(2, 'Sneha', 15000.00),
(3, 'Amit', 5000.00),
(4, 'Zoya', 8000.00),
(5, 'Arjun', 12000.00);

--#1
select * from bank_accounts where balance > 10000;

--#2
INSERT INTO bank_accounts (account_id, account_holder, balance) VALUES
(6, 'Tara', 9000.00);

--#3
update bank_accounts set balance = balance+2000 where account_holder = 'Ravi';
select * from bank_accounts;

--#4
begin;
savepoint start_transaction;
update bank_accounts set balance = balance-3000 where account_holder = 'Sneha';
update bank_accounts set balance = balance+3000 where account_holder = 'Amit';
rollback to savepoint start_transaction;
select * from bank_accounts;

--#5
begin;
update bank_accounts set balance = balance-1000 where account_holder = 'Arjun';
savepoint sp1;
update bank_accounts set balance = balance-2000 where account_holder = 'Zoya';
rollback to savepoint sp1;
commit;
select * from bank_accounts;

--#6
begin;
savepoint sp2;
delete from bank_accounts;
select * from bank_accounts;
rollback to savepoint sp2;
select * from bank_accounts;

--#7
select * from bank_accounts order by balance desc limit 2;

--#8
select avg(balance) from bank_accounts;

--#9
insert into bank_accounts values (1, 'Ravi', 7500.00);
select * from bank_accounts where account_id = 1;

--#10


--#11
CREATE TABLE incoming_transactions (
  account_id INT,
  account_holder VARCHAR(50),
  balance NUMERIC(12, 2)
);
INSERT INTO incoming_transactions (account_id, account_holder, balance) VALUES
(2, 'Sneha', 18000.00),     -- Existing account with updated balance
(6, 'Tara', 9000.00),       -- New account to be inserted
(3, 'Amit', 7000.00);       -- Existing account with updated balance

merge into bank_accounts as b using incoming_transactions as i
on (b.account_holder = i.account_holder)
when matched then
 update set balance = i.balance
when not matched then
 insert values (i.account_id, i.account_holder, i.balance);
select * from bank_accounts;
