"""Tests for MCP server functionality."""

import pytest

from mcp_server_test.server import MCPTestServer


class TestMCPTestServer:
    """Test cases for MCPTestServer."""

    @pytest.fixture
    def server(self) -> MCPTestServer:
        """Create a test server instance."""
        return MCPTestServer()

    def test_server_initialization(self, server: MCPTestServer) -> None:
        """Test that server initializes correctly."""
        assert server.tools == {}
        assert server.resources == {}

    def test_register_tool(self, server: MCPTestServer) -> None:
        """Test tool registration."""
        test_tool = {"name": "test", "description": "A test tool"}
        server.register_tool("test_tool", test_tool)
        
        assert "test_tool" in server.tools
        assert server.tools["test_tool"] == test_tool

    def test_get_tools(self, server: MCPTestServer) -> None:
        """Test getting list of tools."""
        # Initially empty
        assert server.get_tools() == []
        
        # After adding tools
        server.register_tool("tool1", {})
        server.register_tool("tool2", {})
        
        tools = server.get_tools()
        assert len(tools) == 2
        assert "tool1" in tools
        assert "tool2" in tools

    @pytest.mark.asyncio
    async def test_server_start_stop(self, server: MCPTestServer) -> None:
        """Test server start and stop methods."""
        # These should not raise exceptions
        await server.start()
        await server.stop()
