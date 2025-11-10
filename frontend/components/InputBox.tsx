import React, { useState } from 'react';
import { Search, Loader2 } from 'lucide-react';
import { motion } from 'framer-motion';

interface InputBoxProps {
  onSubmit: (query: string) => void;
  isLoading: boolean;
}

const InputBox: React.FC<InputBoxProps> = ({ onSubmit, isLoading }) => {
  const [query, setQuery] = useState('');
  const [isFocused, setIsFocused] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim() && !isLoading) {
      onSubmit(query.trim());
    }
  };

  return (
    <motion.form
      onSubmit={handleSubmit}
      className="w-full max-w-4xl mx-auto"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <div className="relative">
        <div
          className={`flex items-center gap-3 p-4 rounded-xl border-2 transition-all duration-200 ${
            isFocused
              ? 'border-primary-500 shadow-lg shadow-primary-500/20'
              : 'border-gray-300 dark:border-gray-600'
          } bg-white dark:bg-gray-800`}
        >
          <Search className="w-5 h-5 text-gray-400 flex-shrink-0" />
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onFocus={() => setIsFocused(true)}
            onBlur={() => setIsFocused(false)}
            placeholder="Enter job description or paste JD URL..."
            className="flex-1 bg-transparent outline-none text-gray-900 dark:text-gray-100 placeholder-gray-400 dark:placeholder-gray-500"
            disabled={isLoading}
          />
          <button
            type="submit"
            disabled={!query.trim() || isLoading}
            className={`px-6 py-2 rounded-lg font-medium transition-all duration-200 flex items-center gap-2 ${
              query.trim() && !isLoading
                ? 'bg-primary-600 hover:bg-primary-700 text-white shadow-md hover:shadow-lg'
                : 'bg-gray-300 dark:bg-gray-700 text-gray-500 dark:text-gray-400 cursor-not-allowed'
            }`}
          >
            {isLoading ? (
              <>
                <Loader2 className="w-4 h-4 animate-spin" />
                <span>Searching...</span>
              </>
            ) : (
              <span>Get Recommendations</span>
            )}
          </button>
        </div>
      </div>
      <p className="mt-2 text-sm text-gray-500 dark:text-gray-400 text-center">
        Enter a job description or paste a JD URL to get AI-powered assessment recommendations
      </p>
    </motion.form>
  );
};

export default InputBox;

