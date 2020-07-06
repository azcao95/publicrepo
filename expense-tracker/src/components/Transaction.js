import React, { useContext } from "react";
import { GlobalContext } from "../context/GlobalState";

export const Transaction = ({ transaction }) => {
  const { deleteTransaction } = useContext(GlobalContext);

  const sign = transaction.amount < 0 ? "-" : "+";
  const signClassName = transaction.amount < 0 ? "minus" : "plus";

  return (
    <li className={signClassName}>
      {transaction.text}
      <span>
        {sign}${Math.abs(transaction.amount).toFixed(2)}
      </span>
      <button
        onClick={() => deleteTransaction(transaction.id)}
        className="delete=btn"
      >
        x
      </button>
    </li>
  );
};
