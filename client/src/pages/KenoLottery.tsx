
import React, { useEffect, useState } from "react";
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "../components/ui/table";

export default function KenoLottery() {
  interface LotteryNumber {
    id: number;
    draw_date: string;
    created_at: string;
    game_name: string;
    numbers: string;
  }

  const [lotteryNumbers, setLotteryNumbers] = useState<LotteryNumber[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5001/lottery")
      .then((res) => res.json())
      .then((data) => {
        if (Array.isArray(data)) {
          setLotteryNumbers(data);
        } else {
          console.error("Fetched data is not an array:", data);
        }
      })
      .catch((error) => {
        console.error("Error fetching lottery numbers:", error);
      });
  }, []);

  return (
    <>
      <TableCaption>Lottery Numbers.</TableCaption>
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>ID</TableHead>
            <TableHead>Game Name</TableHead>
            <TableHead>Numbers</TableHead>
            <TableHead>Draw Date</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {lotteryNumbers.map((number) => (
            <TableRow key={number.id}>
              <TableCell>{number.id}</TableCell>
              <TableCell>{number.game_name}</TableCell>
              <TableCell>{number.numbers}</TableCell>
              <TableCell>{number.draw_date}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      </>
  );
}