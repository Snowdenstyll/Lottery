// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from "next";

type LotteryNumber = {
  id: number;
  game_name: string;
  draw_date: string;
  draw_time: string;
  numbers: string;
  created_at: string;
};

type Data = {
  lottery_numbers: LotteryNumber[];
};

async function loadLottery(): Promise<Data> {
  const response = await fetch("http://127.0.0.1:5000/lottery");
  if (!response.ok) {
    throw new Error("Failed to load lottery data");
  }
  const data = await response.json();
  return data;
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data | { error: string }>
) {
  try {
    const data = await loadLottery();
    res.status(200).json(data);
  } catch (err) {
    res.status(500).json({ error: "failed to load data" });
  }
}