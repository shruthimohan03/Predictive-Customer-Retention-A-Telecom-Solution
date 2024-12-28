import React, { useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert';
import { Users, AlertTriangle, CheckCircle, Brain, ArrowRightCircle } from 'lucide-react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

// Mock data for demonstration
const mockDissatisfiedCustomers = [
  {
    id: "C1001",
    name: "John Smith",
    dissatisfactionLevel: "High",
    topFeature: "service_outages_3months",
    featureValue: "8 outages",
    strategies: [
      "Schedule immediate network assessment",
      "Provide service credits for downtime",
      "Install network signal booster"
    ]
  },
  {
    id: "C1002",
    name: "Sarah Wilson",
    dissatisfactionLevel: "Moderate",
    topFeature: "missed_payments_6months",
    featureValue: "3 missed",
    strategies: [
      "Offer flexible payment plan",
      "Set up automatic payments",
      "Provide temporary payment relief"
    ]
  },
  {
    id: "C1003",
    name: "Mike Johnson",
    dissatisfactionLevel: "High",
    topFeature: "call_drops_per_month",
    featureValue: "12 drops",
    strategies: [
      "Technical review of coverage area",
      "Offer WiFi calling features",
      "Provide network extender device"
    ]
  }
];

const mockStats = [
  { name: 'Satisfied', value: 750 },
  { name: 'Moderately Dissatisfied', value: 150 },
  { name: 'Highly Dissatisfied', value: 100 }
];

export default function DissatisfactionDashboard() {
  const [selectedCustomer, setSelectedCustomer] = useState(null);
  const [showAIResponse, setShowAIResponse] = useState(false);

  const handleCustomerClick = (customer) => {
    setSelectedCustomer(customer);
    setShowAIResponse(false);
    // Simulate AI processing delay
    setTimeout(() => setShowAIResponse(true), 1000);
  };

  return (
    <div className="p-6 max-w-6xl mx-auto space-y-6">
      {/* Header */}
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Customer Satisfaction Management System</h1>
        <div className="flex items-center gap-2">
          <Users className="w-5 h-5" />
          <span className="font-semibold">1000 Total Customers</span>
        </div>
      </div>

      {/* Overview Stats */}
      <Card>
        <CardHeader>
          <CardTitle>Customer Satisfaction Distribution</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={mockStats}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="value" fill="#4f46e5" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </CardContent>
      </Card>

      {/* Main Content */}
      <div className="grid grid-cols-12 gap-6">
        {/* Dissatisfied Customers List */}
        <div className="col-span-5">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <AlertTriangle className="w-5 h-5 text-red-500" />
                At-Risk Customers
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {mockDissatisfiedCustomers.map((customer) => (
                  <div
                    key={customer.id}
                    onClick={() => handleCustomerClick(customer)}
                    className="p-4 border rounded-lg cursor-pointer hover:bg-gray-50 transition-colors"
                  >
                    <div className="flex justify-between items-start">
                      <div>
                        <h3 className="font-semibold">{customer.name}</h3>
                        <p className="text-sm text-gray-600">ID: {customer.id}</p>
                      </div>
                      <span className={`px-2 py-1 rounded-full text-xs ${
                        customer.dissatisfactionLevel === 'High' 
                          ? 'bg-red-100 text-red-800' 
                          : 'bg-yellow-100 text-yellow-800'
                      }`}>
                        {customer.dissatisfactionLevel}
                      </span>
                    </div>
                    <div className="mt-2 text-sm text-gray-600">
                      Top Issue: {customer.topFeature.replace(/_/g, ' ')}
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>

        {/* AI Analysis and Recommendations */}
        <div className="col-span-7">
          {selectedCustomer ? (
            <div className="space-y-4">
              {/* Customer Details */}
              <Card>
                <CardHeader>
                  <CardTitle>Customer Analysis</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    <div className="flex items-center gap-2">
                      <Users className="w-5 h-5" />
                      <span className="font-semibold">{selectedCustomer.name}</span>
                    </div>
                    <Alert>
                      <AlertTriangle className="h-4 w-4" />
                      <AlertTitle>Primary Issue Detected</AlertTitle>
                      <AlertDescription>
                        {selectedCustomer.topFeature.replace(/_/g, ' ')}: {selectedCustomer.featureValue}
                      </AlertDescription>
                    </Alert>
                  </div>
                </CardContent>
              </Card>

              {/* AI Recommendations */}
              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    <Brain className="w-5 h-5" />
                    AI-Generated Recommendations
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  {showAIResponse ? (
                    <div className="space-y-4">
                      {selectedCustomer.strategies.map((strategy, index) => (
                        <Alert key={index} className="bg-blue-50">
                          <ArrowRightCircle className="h-4 w-4" />
                          <AlertDescription>{strategy}</AlertDescription>
                        </Alert>
                      ))}
                      <div className="mt-4 flex items-center gap-2 text-green-600">
                        <CheckCircle className="w-5 h-5" />
                        <span>Recommendations ready for automation</span>
                      </div>
                    </div>
                  ) : (
                    <div className="flex items-center justify-center h-32">
                      <div className="animate-pulse text-gray-500">
                        AI analyzing customer data...
                      </div>
                    </div>
                  )}
                </CardContent>
              </Card>
            </div>
          ) : (
            <div className="h-full flex items-center justify-center text-gray-500">
              Select a customer to see AI recommendations
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
