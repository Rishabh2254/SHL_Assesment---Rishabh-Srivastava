import React, { useState } from 'react';
import Head from 'next/head';
import { motion } from 'framer-motion';
import { Sparkles, AlertCircle, CheckCircle } from 'lucide-react';
import InputBox from '@/components/InputBox';
import RecommendationTable from '@/components/RecommendationTable';
import Loader from '@/components/Loader';
import { getRecommendations, Recommendation } from '@/utils/api';

export default function Home() {
  const [recommendations, setRecommendations] = useState<Recommendation[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [hasSearched, setHasSearched] = useState(false);

  const handleSearch = async (query: string) => {
    setIsLoading(true);
    setError(null);
    setHasSearched(true);
    setRecommendations([]);

    try {
      const response = await getRecommendations(query);
      setRecommendations(response.recommendations);
    } catch (err: any) {
      setError(err.message || 'An error occurred while fetching recommendations');
      setRecommendations([]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      <Head>
        <title>SHL Assessment Recommendation System</title>
        <meta name="description" content="AI-powered recommendation system for SHL assessments" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>

      <main className="min-h-screen bg-gradient-to-br from-gray-50 via-white to-gray-100 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900">
        <div className="container mx-auto px-4 py-12">
          {/* Header */}
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            className="text-center mb-12"
          >
            <div className="flex items-center justify-center gap-3 mb-4">
              <Sparkles className="w-8 h-8 text-primary-600 dark:text-primary-400" />
              <h1 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white">
                SHL Assessment Recommender
              </h1>
            </div>
            <p className="text-lg text-gray-600 dark:text-gray-300 mt-2">
              AI-Powered Recommendation System for SHL Assessments
            </p>
          </motion.div>

          {/* Input Box */}
          <InputBox onSubmit={handleSearch} isLoading={isLoading} />

          {/* Loading State */}
          {isLoading && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="flex flex-col items-center justify-center mt-12 gap-4"
            >
              <Loader size="lg" />
              <p className="text-gray-600 dark:text-gray-400">
                Analyzing your query and finding the best assessments...
              </p>
            </motion.div>
          )}

          {/* Error State */}
          {error && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="max-w-4xl mx-auto mt-8 p-4 bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-xl"
            >
              <div className="flex items-center gap-3">
                <AlertCircle className="w-5 h-5 text-red-600 dark:text-red-400 flex-shrink-0" />
                <div>
                  <h3 className="font-semibold text-red-800 dark:text-red-300">Error</h3>
                  <p className="text-sm text-red-700 dark:text-red-400 mt-1">{error}</p>
                </div>
              </div>
            </motion.div>
          )}

          {/* Success State */}
          {!isLoading && !error && hasSearched && recommendations.length === 0 && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="max-w-4xl mx-auto mt-8 p-4 bg-yellow-50 dark:bg-yellow-900/20 border border-yellow-200 dark:border-yellow-800 rounded-xl"
            >
              <div className="flex items-center gap-3">
                <AlertCircle className="w-5 h-5 text-yellow-600 dark:text-yellow-400 flex-shrink-0" />
                <p className="text-sm text-yellow-700 dark:text-yellow-400">
                  No recommendations found. Please try a different query.
                </p>
              </div>
            </motion.div>
          )}

          {/* Recommendations Table */}
          {!isLoading && !error && recommendations.length > 0 && (
            <>
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="max-w-4xl mx-auto mt-8 p-4 bg-green-50 dark:bg-green-900/20 border border-green-200 dark:border-green-800 rounded-xl"
              >
                <div className="flex items-center gap-3">
                  <CheckCircle className="w-5 h-5 text-green-600 dark:text-green-400 flex-shrink-0" />
                  <p className="text-sm text-green-700 dark:text-green-400">
                    Found {recommendations.length} relevant assessment{recommendations.length !== 1 ? 's' : ''}
                  </p>
                </div>
              </motion.div>
              <RecommendationTable recommendations={recommendations} />
            </>
          )}

          {/* Footer */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.5 }}
            className="text-center mt-16 text-sm text-gray-500 dark:text-gray-400"
          >
            <p>SHL Assessment Recommendation System - Powered by AI</p>
          </motion.div>
        </div>
      </main>
    </>
  );
}

