/**
 * API utility functions for communicating with the backend
 */

import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface Recommendation {
  assessment_name: string;
  assessment_url: string;
}

export interface RecommendationsResponse {
  recommendations: Recommendation[];
}

export interface HealthResponse {
  status: string;
}

/**
 * Check if the API is healthy
 */
export async function checkHealth(): Promise<HealthResponse> {
  try {
    const response = await axios.get<HealthResponse>(`${API_URL}/health`);
    return response.data;
  } catch (error) {
    console.error('Health check failed:', error);
    throw error;
  }
}

/**
 * Get recommendations for a query
 */
export async function getRecommendations(query: string): Promise<RecommendationsResponse> {
  try {
    const response = await axios.post<RecommendationsResponse>(
      `${API_URL}/recommend`,
      { query },
      {
        headers: {
          'Content-Type': 'application/json',
        },
        timeout: 30000, // 30 second timeout
      }
    );
    return response.data;
  } catch (error: any) {
    console.error('Failed to get recommendations:', error);
    if (error.response) {
      throw new Error(error.response.data.detail || 'Failed to get recommendations');
    } else if (error.request) {
      throw new Error('No response from server. Please check if the backend is running.');
    } else {
      throw new Error(error.message || 'An unexpected error occurred');
    }
  }
}

