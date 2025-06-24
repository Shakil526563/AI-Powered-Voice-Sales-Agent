#!/usr/bin/env python3
"""
Test script to verify that the RAG system is working correctly
"""
import sys
import traceback

def test_rag_system():
    """Test the RAG system functionality"""
    try:
        print("🔄 Testing RAG system...")
        
        # Import and initialize the LLM service
        from llm_service import LLMService
        
        service = LLMService()
        
        if not service.rag_enabled:
            print(f" RAG system not enabled. Error: {service.rag_error}")
            return False
        
        print(" RAG system enabled successfully")
          # Test a simple query
        test_query = "What is the AI Mastery Bootcamp about?"
        
        try:
            response = service.generate_response([], test_query)
            print(f" Test query successful")
            print(f"Query: {test_query}")
            print(f"Response: {response}")
            return True
            
        except Exception as e:
            print(f" Error generating response: {e}")
            traceback.print_exc()
            return False
            
    except Exception as e:
        print(f" Error testing RAG system: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_rag_system()
    if success:
        print("\n RAG system test passed!")
        sys.exit(0)
    else:
        print("\n RAG system test failed!")
        sys.exit(1)
