"use client"

import React, { useState } from 'react'
import { Bell, Calendar, Home, LineChart, Moon, Sun, User } from 'lucide-react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Progress } from "@/components/ui/progress"
import { ChartContainer, ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
import { Area, AreaChart, CartesianGrid, ResponsiveContainer, XAxis, YAxis, Legend } from 'recharts'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

// Mock data for sleep monitoring
const sleepData = [
  { time: '22:00', awake: 1, rem: 0, light: 0, deep: 0 },
  { time: '23:00', awake: 0.2, rem: 0, light: 0.8, deep: 0 },
  { time: '00:00', awake: 0, rem: 0, light: 0.3, deep: 0.7 },
  { time: '01:00', awake: 0, rem: 0, light: 0, deep: 1 },
  { time: '02:00', awake: 0, rem: 0.6, light: 0.4, deep: 0 },
  { time: '03:00', awake: 0, rem: 0.8, light: 0.2, deep: 0 },
  { time: '04:00', awake: 0, rem: 0, light: 0.5, deep: 0.5 },
  { time: '05:00', awake: 0, rem: 0.7, light: 0.3, deep: 0 },
  { time: '06:00', awake: 0.1, rem: 0.9, light: 0, deep: 0 },
  { time: '07:00', awake: 1, rem: 0, light: 0, deep: 0 },
]

// Mock data for energy levels
const energyData = [
  { time: '06:00', level: 3 },
  { time: '09:00', level: 7 },
  { time: '12:00', level: 6 },
  { time: '15:00', level: 4 },
  { time: '18:00', level: 5 },
  { time: '21:00', level: 3 },
]

// Mock data for mood and productivity
const generateMonthData = () => {
  const data = []
  const now = new Date()
  for (let i = 0; i < 30; i++) {
    const date = new Date(now.getFullYear(), now.getMonth(), now.getDate() - i)
    data.unshift({
      date: date.toISOString().split('T')[0],
      mood: Math.floor(Math.random() * 5) + 1,
      productivity: Math.floor(Math.random() * 5) + 1,
    })
  }
  return data
}

const monthData = generateMonthData()

export default function Dashboard() {
  const [activeTab, setActiveTab] = useState('home')

  const renderGithubLikeGraph = (data, key) => {
    const colorScale = ['#4c1d95', '#5b21b6', '#6d28d9', '#7c3aed', '#8b5cf6']
    return (
      <div>
        <div className="grid grid-cols-7 gap-1">
          {data.map((day, index) => (
            <div
              key={index}
              className="w-4 h-4 rounded-sm"
              style={{
                backgroundColor: colorScale[day[key] - 1],
              }}
              title={`Date: ${day.date}, ${key.charAt(0).toUpperCase() + key.slice(1)}: ${day[key]}/5`}
            />
          ))}
        </div>
        <div className="mt-2 flex justify-between">
          {colorScale.map((color, index) => (
            <div key={index} className="flex items-center">
              <div className="w-3 h-3 rounded-sm mr-1" style={{ backgroundColor: color }}></div>
              <span className="text-xs text-gray-400">{index + 1}</span>
            </div>
          ))}
        </div>
      </div>
    )
  }

  return (
    <div className="flex h-screen bg-black text-white">
      {/* Sidebar */}
      <aside className="w-64 bg-zinc-900 border-r border-zinc-800">
        <div className="p-4">
          <h1 className="text-2xl font-bold text-white">RestIQ</h1>
        </div>
        <nav className="mt-6">
          {[
            { icon: Home, label: 'Home', id: 'home' },
            { icon: Moon, label: 'Sleep', id: 'sleep' },
            { icon: Sun, label: 'Energy', id: 'energy' },
            { icon: LineChart, label: 'Productivity', id: 'productivity' },
            { icon: Calendar, label: 'Mood', id: 'mood' },
          ].map((item) => (
            <Button
              key={item.id}
              variant={activeTab === item.id ? 'secondary' : 'ghost'}
              className={`w-full justify-start text-sm font-medium transition-colors hover:text-white hover:bg-zinc-800/50 ${
                activeTab === item.id ? 'text-white bg-zinc-800' : 'text-zinc-400'
              }`}
              onClick={() => setActiveTab(item.id)}
            >
              <item.icon className="mr-2 h-4 w-4" />
              {item.label}
            </Button>
          ))}
        </nav>
      </aside>

      {/* Main content */}
      <main className="flex-1 overflow-y-auto">
        <div className="border-b border-zinc-800">
          <header className="flex h-14 items-center px-4 lg:px-8">
            <h2 className="text-lg font-semibold">Dashboard</h2>
            <div className="ml-auto flex items-center space-x-4">
              <Select defaultValue="today">
                <SelectTrigger className="w-[180px] bg-zinc-900 text-white border-zinc-700">
                  <SelectValue placeholder="Select timeframe" />
                </SelectTrigger>
                <SelectContent className="bg-zinc-900 text-white border-zinc-700">
                  <SelectItem value="today">Today</SelectItem>
                  <SelectItem value="week">This Week</SelectItem>
                  <SelectItem value="month">This Month</SelectItem>
                </SelectContent>
              </Select>
              <Button variant="ghost" size="icon" className="text-zinc-400 hover:text-white hover:bg-zinc-800">
                <Bell className="h-5 w-5" />
              </Button>
              <Button variant="ghost" size="icon" className="text-zinc-400 hover:text-white hover:bg-zinc-800">
                <User className="h-5 w-5" />
              </Button>
            </div>
          </header>
        </div>

        <div className="p-4 lg:p-8 space-y-8">
          {/* Sleep Monitoring Chart */}
          <Card className="bg-zinc-900 border-zinc-800">
            <CardHeader>
              <CardTitle className="text-white">Sleep Monitoring</CardTitle>
              <CardDescription className="text-zinc-400">Sleep intensity levels throughout the night</CardDescription>
            </CardHeader>
            <CardContent>
              <ChartContainer
                config={{
                  awake: {
                    label: "Awake",
                    color: "#ef4444",
                  },
                  rem: {
                    label: "REM Sleep",
                    color: "#3b82f6",
                  },
                  light: {
                    label: "Light Sleep",
                    color: "#22c55e",
                  },
                  deep: {
                    label: "Deep Sleep",
                    color: "#8b5cf6",
                  },
                }}
                className="h-[300px] w-full"
              >
                <ResponsiveContainer width="100%" height="100%">
                  <AreaChart data={sleepData} stackOffset="expand">
                    <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
                    <XAxis dataKey="time" stroke="#9ca3af" />
                    <YAxis tickFormatter={(value) => `${(value * 100).toFixed(0)}%`} stroke="#9ca3af" />
                    <ChartTooltip content={<ChartTooltipContent />} />
                    <Legend />
                    <Area type="monotone" dataKey="awake" stackId="1" stroke="#ef4444" fill="#ef4444" />
                    <Area type="monotone" dataKey="rem" stackId="1" stroke="#3b82f6" fill="#3b82f6" />
                    <Area type="monotone" dataKey="light" stackId="1" stroke="#22c55e" fill="#22c55e" />
                    <Area type="monotone" dataKey="deep" stackId="1" stroke="#8b5cf6" fill="#8b5cf6" />
                  </AreaChart>
                </ResponsiveContainer>
              </ChartContainer>
            </CardContent>
          </Card>

          {/* Energy Levels Chart */}
          <Card className="bg-zinc-900 border-zinc-800">
            <CardHeader>
              <CardTitle className="text-white">Energy Levels</CardTitle>
              <CardDescription className="text-zinc-400">Energy levels throughout the day</CardDescription>
            </CardHeader>
            <CardContent>
              <ChartContainer
                config={{
                  level: {
                    label: "Energy Level",
                    color: "#f59e0b",
                  },
                }}
                className="h-[300px] w-full"
              >
                <ResponsiveContainer width="100%" height="100%">
                  <AreaChart data={energyData}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
                    <XAxis dataKey="time" stroke="#9ca3af" />
                    <YAxis stroke="#9ca3af" />
                    <ChartTooltip content={<ChartTooltipContent />} />
                    <Legend />
                    <Area type="monotone" dataKey="level" stroke="#f59e0b" fill="#f59e0b" fillOpacity={0.3} />
                  </AreaChart>
                </ResponsiveContainer>
              </ChartContainer>
            </CardContent>
          </Card>

          {/* Mood and Productivity Trackers */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <Card className="bg-zinc-900 border-zinc-800">
              <CardHeader>
                <CardTitle className="text-white">Mood Tracker</CardTitle>
                <CardDescription className="text-zinc-400">Monthly mood data</CardDescription>
              </CardHeader>
              <CardContent>
                {renderGithubLikeGraph(monthData, 'mood')}
              </CardContent>
            </Card>

            <Card className="bg-zinc-900 border-zinc-800">
              <CardHeader>
                <CardTitle className="text-white">Productivity Tracker</CardTitle>
                <CardDescription className="text-zinc-400">Monthly productivity data</CardDescription>
              </CardHeader>
              <CardContent>
                {renderGithubLikeGraph(monthData, 'productivity')}
              </CardContent>
            </Card>
          </div>

          {/* Quick Stats */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
            <Card className="bg-zinc-900 border-zinc-800">
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium text-white">Avg. Sleep</CardTitle>
                <Moon className="h-4 w-4 text-zinc-400" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold text-white">7.4 hrs</div>
                <Progress value={74} className="mt-2" />
              </CardContent>
            </Card>
            <Card className="bg-zinc-900 border-zinc-800">
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium text-white">Avg. Energy</CardTitle>
                <Sun className="h-4 w-4 text-zinc-400" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold text-white">6.5/10</div>
                <Progress value={65} className="mt-2" />
              </CardContent>
            </Card>
            <Card className="bg-zinc-900 border-zinc-800">
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium text-white">Avg. Mood</CardTitle>
                <User className="h-4 w-4 text-zinc-400" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold text-white">3.7/5</div>
                <Progress value={74} className="mt-2" />
              </CardContent>
            </Card>
            <Card className="bg-zinc-900 border-zinc-800">
              <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                <CardTitle className="text-sm font-medium text-white">Avg. Productivity</CardTitle>
                <LineChart className="h-4 w-4 text-zinc-400" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold text-white">77%</div>
                <Progress value={77} className="mt-2" />
              </CardContent>
            </Card>
          </div>
        </div>
      </main>
    </div>
  )
}